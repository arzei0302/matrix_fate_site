from django.conf import settings
import fitz
import os
import tempfile

from matrix_fate.utils.positions import positions


def get_text_width(text, font_obj, fontsize):
    return font_obj.text_length(str(text), fontsize)


def insert_centered_text(page, text, center_x, y,
                         fontname_regular, fontname_bold,
                         font_obj_regular, font_obj_bold,
                         fontsize=12, color=(0.0, 0.392, 0.0), is_bold=False):
    text = str(text).strip()
    if not text:
        return

    font_obj = font_obj_bold if is_bold else font_obj_regular
    fontname = fontname_bold if is_bold else fontname_regular

    width = get_text_width(text, font_obj, fontsize)
    x = center_x - width / 2
    page.insert_text(
        (x, y),
        text,
        fontname=fontname,
        fontsize=fontsize,
        overlay=True,
        render_mode=0,
        color=color
    )


def fill_matrix_pdf(data: dict) -> str:
    pdf_path = "./files/new_matrix_scheme.pdf"
    font_path_regular = os.path.join(settings.BASE_DIR, "matrix_fate", "font", "DejaVuSans.ttf")
    font_path_bold = os.path.join(settings.BASE_DIR, "matrix_fate", "font", "DejaVuSans-Bold.ttf")


    if not os.path.exists(pdf_path):
        raise FileNotFoundError(f"PDF файл не найден: {pdf_path}")
    if not os.path.exists(font_path_regular):
        raise FileNotFoundError(f"Файл шрифта не найден: {font_path_regular}")
    if not os.path.exists(font_path_bold):
        raise FileNotFoundError(f"Файл шрифта не найден: {font_path_bold}")

    base_pdf = fitz.open(pdf_path)
    page = base_pdf[0]

    # Регистрируем оба шрифта
    page.insert_font(fontname="Regular", fontfile=font_path_regular)
    page.insert_font(fontname="Bold", fontfile=font_path_bold)

    font_obj_regular = fitz.Font(fontfile=font_path_regular)
    font_obj_bold = fitz.Font(fontfile=font_path_bold)

    result_data = data.get("result_data", data)
    if "matrix" in result_data:
        result_data = result_data["matrix"]

    if not isinstance(result_data, dict):
        raise ValueError("Ожидался словарь с матрицей")

    for pos in positions:
        if len(pos) == 4:
            key, x, y, fontsize = pos
            is_bold = False
        elif len(pos) == 5:
            key, x, y, fontsize, is_bold = pos
        else:
            raise ValueError(f"Неверный формат позиции: {pos}")

        text = str(result_data.get(key, "")).strip()
        insert_centered_text(
            page, text, x, y,
            "Regular", "Bold",
            font_obj_regular, font_obj_bold,
            fontsize, is_bold=is_bold
        )

    page.wrap_contents()
    filled_pdf_path = tempfile.NamedTemporaryFile(delete=False, suffix=".pdf").name
    base_pdf.save(filled_pdf_path)
    base_pdf.close()
    return filled_pdf_path

