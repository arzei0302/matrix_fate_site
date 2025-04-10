import os
import random
from django.core.management.base import BaseCommand

from other_app.models import ArcanaClues



IMAGE_NAME = 'placeholder.png'
IMAGE_PATH = os.path.join('past_cards', IMAGE_NAME)

TITLES = [
    f"Карта {i}" for i in range(1, 79)
]
DESCRIPTIONS = [
    f"Описание для карты номер {i}. Это пример описания, которое будет отображаться в карточке."
    for i in range(1, 22)
]

class Command(BaseCommand):
    help = "Заполняет базы данных случайными записями для ArcanaClues"

    def handle(self, *args, **kwargs):
        self.stdout.write("Очистка таблиц...")
        ArcanaClues.objects.all().delete()

        self.stdout.write("Добавление новых записей...")

        for i in range(78):
            title = random.choice(TITLES)
            description = random.choice(DESCRIPTIONS)

            ArcanaClues.objects.create(
                title=title,
                description=description,
                image=IMAGE_PATH
            )
            

        self.stdout.write(self.style.SUCCESS("Заполнение таблиц завершено!"))
