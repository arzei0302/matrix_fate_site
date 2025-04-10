# import tempfile
# import subprocess
# import io
# import fitz
# from pathlib import Path
# from PyPDF2 import PdfMerger
# from PIL import Image

# from .matrix_fate_report import fill_matrix_template
# from .fill_pdf import fill_matrix_pdf


# def render_pdf_page_to_image(pdf_path: str, dpi=150) -> Path:
#     pdf = fitz.open(pdf_path)
#     page = pdf[0]
#     mat = fitz.Matrix(dpi / 72, dpi / 72)
#     pix = page.get_pixmap(matrix=mat)

#     img_path = Path(tempfile.NamedTemporaryFile(delete=False, suffix=".png").name)
#     pix.save(str(img_path))
#     return img_path


# def convert_png_to_pdf(png_path: Path) -> Path:
#     image = Image.open(png_path)
#     rgb_image = image.convert("RGB")
#     pdf_path = Path(tempfile.NamedTemporaryFile(delete=False, suffix=".pdf").name)
#     rgb_image.save(pdf_path, "PDF", resolution=150.0)
#     return pdf_path


# def generate_full_matrix_pdf(matrix_values: dict) -> io.BytesIO:
#     try:
#         visual_pdf_path = fill_matrix_pdf(matrix_values)
#         docx_file = tempfile.NamedTemporaryFile(delete=False, suffix=".docx")
#         docx_path = Path(docx_file.name)
#         template_path = Path("/home/arzei/matrix_fate/files/matrix_fate_report.docx")
#         fill_matrix_template(matrix_values, template_path, docx_path)

#         text_pdf_path = docx_path.with_suffix(".pdf")
#         subprocess.run([
#             "libreoffice", "--headless",
#             "--convert-to", "pdf", str(docx_path),
#             "--outdir", str(docx_path.parent)
#         ], check=True)

#         merger = PdfMerger()
#         merger.append(visual_pdf_path)
#         merger.append(str(text_pdf_path))

#         final_pdf = tempfile.NamedTemporaryFile(delete=False, suffix=".pdf")
#         with open(final_pdf.name, "wb") as fout:
#             merger.write(fout)
#         merger.close()

#         with open(final_pdf.name, "rb") as f:
#             result_buffer = io.BytesIO(f.read())
#         result_buffer.seek(0)
#         return result_buffer

#     except Exception as e:
#         raise Exception(f"Ошибка генерации полного PDF: {e}")


# from django.http import FileResponse
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status

# class FullMatrixPDFView(APIView):
#     def post(self, request):
#         try:
#             pdf_buffer = generate_full_matrix_pdf(request.data)
#             return FileResponse(pdf_buffer, filename="matrix_result.pdf", as_attachment=True)
#         except Exception as e:
#             return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

