import random
from django.core.management.base import BaseCommand
from faker import Faker

from prognosis_app.models import (
    GeneralPrognosis, January, February, March, April, May, June, July,
    August, September, October, November, December,
)

fake = Faker("fi_FI")

ORDER_IDS = list(range(1, 23))

MODELS = [
    (GeneralPrognosis, "Yleinen ennuste"),
    (January, "Tammikuu"),
    (February, "Helmikuu"),
    (March, "Maaliskuu"),
    (April, "Huhtikuu"),
    (May, "Toukokuu"),
    (June, "Kesäkuu"),
    (July, "Heinäkuu"),
    (August, "Elokuu"),
    (September, "Syyskuu"),
    (October, "Lokakuu"),
    (November, "Marraskuu"),
    (December, "Joulukuu"),
]

class Command(BaseCommand):
    help = "Täyttää ennustetietokannat satunnaisilla tiedoilla."

    def handle(self, *args, **kwargs):
        for model, month_name in MODELS:
            for order_id in ORDER_IDS:
                instance = model.objects.create(
                    title=f"Ennuste kuukaudelle {month_name} (Arkaani {order_id})",
                    description=fake.paragraph(nb_sentences=5),
                    order_id=order_id
                )
                self.stdout.write(self.style.SUCCESS(f"✔ {month_name}: Lisätty ennuste, jossa order_id={order_id}"))
        
        self.stdout.write(self.style.SUCCESS("✅ Tietojen täyttäminen valmis!"))

# python manage.py populate_prognosis