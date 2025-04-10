import random
from django.core.management.base import BaseCommand
from faker import Faker

from finance_app.models import (
    FinanceCategory, TheMainTask40Years, WhatBeforeYouTurn40Years, WhatAfterYouTurn40Years
)

fake = Faker("ru_RU")

ORDER_IDS = list(range(1, 23))

MODELS = [
    (TheMainTask40Years, "Главная задача 40 лет"),
    (WhatBeforeYouTurn40Years, "Что нужно сделать до 40 лет"),
    (WhatAfterYouTurn40Years, "Что нужно сделать после 40 лет"),
]

class Command(BaseCommand):
    help = "Заполняет модели Кармы и Задачи 40 лет случайными данными."

    def handle(self, *args, **kwargs):
        try:
            category = FinanceCategory.objects.get(id=6, title="Карма и задача 40 лет")
        except FinanceCategory.DoesNotExist:
            self.stdout.write(self.style.ERROR("❌ Категория с id=6 ('Карма и задача 40 лет') не найдена!"))
            return

        for model, model_name in MODELS:
            for order_id in ORDER_IDS:
                instance = model.objects.create(
                    category=category,
                    title=f"{model_name} (Аркан {order_id})",
                    description=fake.paragraph(nb_sentences=5),
                    order_id=order_id
                )
                self.stdout.write(self.style.SUCCESS(f"✔ {model_name}: Добавлен прогноз с order_id={order_id}"))

        self.stdout.write(self.style.SUCCESS("✅ Заполнение завершено!"))

# python manage.py populate_karma_and_task_40
