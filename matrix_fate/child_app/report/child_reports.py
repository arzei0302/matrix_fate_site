import tempfile
import subprocess
import io
import fitz
from pathlib import Path
from PyPDF2 import PdfMerger
from PIL import Image
from django.http import FileResponse
from django.db.models import Q
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework import serializers
from drf_spectacular.utils import extend_schema, OpenApiExample

from django.conf import settings
from matrix_fate.child_app.report.fill_pdf_child import fill_matrix_pdf
from matrix_fate.child_app.report.fill_word_child import fill_matrix_template
from matrix_fate.matrix_auth_app.models import UserCalculationHistory
from matrix_fate.matrix_auth_app.models import CustomUser

#
def render_pdf_page_to_image(pdf_path: str, dpi=150) -> Path:
    pdf = fitz.open(pdf_path)
    page = pdf[0]
    mat = fitz.Matrix(dpi / 72, dpi / 72)
    pix = page.get_pixmap(matrix=mat)

    img_path = Path(tempfile.NamedTemporaryFile(delete=False, suffix=".png").name)
    pix.save(str(img_path))
    return img_path


def convert_png_to_pdf(png_path: Path) -> Path:
    image = Image.open(png_path)
    rgb_image = image.convert("RGB")
    pdf_path = Path(tempfile.NamedTemporaryFile(delete=False, suffix=".pdf").name)
    rgb_image.save(pdf_path, "PDF", resolution=150.0)
    return pdf_path


def generate_full_matrix_pdf(
        history_record: UserCalculationHistory
    ) -> io.BytesIO:
    try:
        matrix_values = history_record.result_data
        input_data = history_record.input_data
        category = history_record.category
        profile = history_record.profile

        matrix_values["day"] = f"{input_data.get('day'):02}"
        matrix_values["month"] = f"{input_data.get('month'):02}"
        matrix_values["year"] = str(input_data.get('year'))

        visual_pdf_path = fill_matrix_pdf(matrix_values)

        docx_file = tempfile.NamedTemporaryFile(delete=False, suffix=".docx")
        docx_path = Path(docx_file.name)
        template_path = settings.REPORT_TEMPLATES_DIR / "child_report.docx"


        fill_matrix_template(matrix_values, template_path, docx_path)

        text_pdf_path = docx_path.with_suffix(".pdf")
        subprocess.run([
            "libreoffice", "--headless",
            "--convert-to", "pdf", str(docx_path),
            "--outdir", str(docx_path.parent)
        ], check=True)

        merger = PdfMerger()
        merger.append(visual_pdf_path)
        merger.append(str(text_pdf_path))

        final_pdf = tempfile.NamedTemporaryFile(delete=False, suffix=".pdf")
        with open(final_pdf.name, "wb") as fout:
            merger.write(fout)
        merger.close()

        with open(final_pdf.name, "rb") as f:
            result_buffer = io.BytesIO(f.read())
        result_buffer.seek(0)
        return result_buffer

    except Exception as e:
        raise Exception(f"Ошибка генерации полного PDF: {e}")
    

class ChildPDFInputSerializer(serializers.Serializer):
    email = serializers.EmailField(
        required=False, 
        help_text="Email пользователя")
    history_id = serializers.IntegerField(
        required=False, help_text="ID истории расчёта")
    category = serializers.CharField(
        required=False, default="matrix_fate", 
        help_text="Категория расчёта: matrix_fate")
    input_data = serializers.DictField(
        child=serializers.IntegerField(),
        required=False,
        help_text="Входные данные для поиска расчета (day, month, year)"
    )


class FullChildPDFView(APIView):
    permission_classes = [IsAuthenticated]

    @extend_schema(
        summary="Скачать PDF 'Детская",
        description="PDF-документ на основе данных истории расчёта.(категория только child)",
        request=ChildPDFInputSerializer,
        tags=["Matrix Fate Reports"],
        examples=[
            OpenApiExample(
                name="Поиск по input_data",
                value={
                    "email": "example@gmail.com",
                    "input_data": {
                        "day": 1,
                        "month": 1,
                        "year": 2025
                    }
                },
                request_only=True
            ),
            OpenApiExample(
                name="Поиск по history_id",
                value={
                    "history_id": 12
                },
                request_only=True
            ),
        ]
    )

    def post(self, request):
        try:
            # 1. Получение email из запроса (если передан)
            email = request.data.get("email")
            if email:
                user = CustomUser.objects.filter(email=email).first()
                if not user:
                    return Response({"error": "Пользователь с таким email не найден"}, status=404)
                profile = user.profile
            else:
                profile = request.user.profile

            # 2. Остальная логика
            history_id = request.data.get("history_id")
            category = request.data.get("category", "child")
            input_data = request.data.get("input_data", {})

            history_record = None

            if history_id:
                history_record = UserCalculationHistory.objects.get(id=history_id, profile=profile)

            elif category and input_data:
                try:
                    history_record = UserCalculationHistory.objects.filter(
                        profile=profile,
                        category=category,
                        input_data=input_data
                    ).latest("created_at")
                except UserCalculationHistory.DoesNotExist:
                    pass

                if not history_record:
                    day = input_data.get("day")
                    month = input_data.get("month")
                    year = input_data.get("year")
                    if day and month and year:
                        try:
                            history_record = UserCalculationHistory.objects.filter(
                                profile=profile,
                                category=category,
                                input_data__day=day,
                                input_data__month=month,
                                input_data__year=year
                            ).latest("created_at")
                        except UserCalculationHistory.DoesNotExist:
                            pass

            elif category:
                history_record = UserCalculationHistory.objects.filter(
                    profile=profile,
                    category=category
                ).latest("created_at")

            if not history_record:
                return Response({"error": "Расчёт не найден"}, status=404)

            pdf_buffer = generate_full_matrix_pdf(history_record)
            return FileResponse(pdf_buffer, filename="child_report.pdf", as_attachment=True)

        except Exception as e:
            return Response({"error": str(e)}, status=500)
