import fitz
import os
import tempfile

from utils.positions import positions


def get_text_width(text, font_obj, fontsize):
    return font_obj.text_length(str(text), fontsize)


def insert_centered_text(page, text, center_x, y, fontname, font_obj, fontsize=12, color=(0.0, 0.392, 0.0)):
    text = str(text).strip()
    if not text:
        return
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
    pdf_path = "./files/final_matrix_schema3_test.pdf"
    font_path = "./font/DejaVuSans.ttf"
    font_alias = "Bold"

    if not os.path.exists(pdf_path):
        raise FileNotFoundError(f"PDF файл не найден: {pdf_path}")
    if not os.path.exists(font_path):
        raise FileNotFoundError(f"Файл шрифта не найден: {font_path}")

    base_pdf = fitz.open(pdf_path)
    page = base_pdf[0]
    original_rect = page.rect
    cropped_rect = fitz.Rect(original_rect.x0, original_rect.y0, original_rect.x1, original_rect.y1 - 400)
    page.set_cropbox(cropped_rect)
    page.insert_font(fontname=font_alias, fontfile=font_path)
    font_obj = fitz.Font(fontfile=font_path)

    result_data = data.get("result_data", data)
    if "matrix" in result_data:
        result_data = result_data["matrix"]

    if not isinstance(result_data, dict):
        raise ValueError("Ожидался словарь с матрицей")

    for key, x, y, fontsize in positions:
        text = str(result_data.get(key, "")).strip()
        insert_centered_text(page, text, x, y, font_alias, font_obj, fontsize)
        

    page.wrap_contents()
    filled_pdf_path = tempfile.NamedTemporaryFile(delete=False, suffix=".pdf").name
    base_pdf.save(filled_pdf_path)
    base_pdf.close()
    return filled_pdf_path
