from PIL import Image

# Замените 'input.png' на путь к вашему файлу
# input_file = '/home/arzei/Рабочий стол/news_matrix_scheme.png'
# input_file = '/home/arzei/test_notif/Изображения/compatibility_scheme1.png'
input_file = '/home/arzei/test_notif/Изображения/compatibility_scheme2.png'

output_file = 'output2.pdf'

# Открываем PNG-файл
image = Image.open(input_file)

# Конвертируем в RGB (PDF не поддерживает прозрачность)
rgb_image = image.convert('RGB')

# Сохраняем как PDF
rgb_image.save(output_file)

print(f"Файл успешно сохранён как {output_file}")
