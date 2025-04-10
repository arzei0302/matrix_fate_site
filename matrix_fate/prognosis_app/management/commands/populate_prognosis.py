import random
from django.core.management.base import BaseCommand
from faker import Faker

from prognosis_app.models import (
    GeneralPrognosis, January, February, March, April, May, June, July,
    August, September, October, November, December,
)

fake = Faker("ru_RU")

ORDER_IDS = list(range(1, 23))

MODELS = [
    (GeneralPrognosis, "Общий прогноз"),
    (January, "Январь"),
    (February, "Февраль"),
    (March, "Март"),
    (April, "Апрель"),
    (May, "Май"),
    (June, "Июнь"),
    (July, "Июль"),
    (August, "Август"),
    (September, "Сентябрь"),
    (October, "Октябрь"),
    (November, "Ноябрь"),
    (December, "Декабрь"),
]

class Command(BaseCommand):
    help = "Заполняет базы данных прогнозов случайными данными."

    def handle(self, *args, **kwargs):
        for model, month_name in MODELS:
            for order_id in ORDER_IDS:
                instance = model.objects.create(
                    title=f"Прогноз для {month_name} (Аркан {order_id})",
                    description=fake.paragraph(nb_sentences=5),
                    order_id=order_id
                )
                self.stdout.write(self.style.SUCCESS(f"✔ {month_name}: Добавлен прогноз с order_id={order_id}"))
        
        self.stdout.write(self.style.SUCCESS("✅ Заполнение завершено!"))


# python manage.py populate_prognosis

