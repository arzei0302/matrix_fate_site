import os
import random
from django.core.management.base import BaseCommand

from other_app.models import FinancialAndAntiCodeCalculation



IMAGE_NAME = 'placeholder.png'
IMAGE_PATH = os.path.join('past_cards', IMAGE_NAME)

TITLES = [
    f"Рассчет фин и анти кода{i}" for i in range(1, 79)
]
DESCRIPTIONS = [
    f"Описание рассчета фин и анти кода номер {i}. Это пример описания, которое будет отображаться в карточке."
    for i in range(1, 79)  # Было 22, теперь 79 (равно `TITLES`)
]


class Command(BaseCommand):
    help = "Заполняет базу данных случайными записями для FinancialAndAntiCodeCalculation"

    def handle(self, *args, **kwargs):
        self.stdout.write("Очистка таблиц...")
        FinancialAndAntiCodeCalculation.objects.all().delete()

        self.stdout.write("Добавление новых записей...")

        for i in range(78):
            title = random.choice(TITLES)
            description = random.choice(DESCRIPTIONS)

            FinancialAndAntiCodeCalculation.objects.create(
                title=title,
                description=description,
                image=IMAGE_PATH,  # ✅ Добавлена запятая
                order_id = random.randint(1, 22)

)

            

        self.stdout.write(self.style.SUCCESS("Заполнение таблиц завершено!"))
