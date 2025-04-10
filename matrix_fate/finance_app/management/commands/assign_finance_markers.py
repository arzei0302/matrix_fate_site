from django.core.management.base import BaseCommand
from finance_app.models import(
    YourGreatestTalentBirth, QualitiesRevealedAge20, QualitiesDevelopAge40,

     YourOpportunity,

     TaskPersonalArcana1, TaskPersonalArcana2, TaskPersonalArcana3,

     TheMainTask40Years, WhatBeforeYouTurn40Years, WhatAfterYouTurn40Years,

     WhatGivesYouMoney, WhatOpensYourMoneyChannel, AreasOfRealization,

     TasksOpenMoneyChannel1, TasksOpenMoneyChannel2, WhatBlocksMoneyEnergy,
)

from django.db import transaction


class Command(BaseCommand):
    help = "Назначает маркеры (a, b, c и т.д.) объектам с order_id"

    def handle(self, *args, **options):
        # Сопоставление: (модель, маркер)
        model_marker_map = [
            (YourGreatestTalentBirth, "a"),
            (QualitiesRevealedAge20, "b"),
            (QualitiesDevelopAge40, "c"),

            (YourOpportunity, "a2"),

            (TaskPersonalArcana1, "t"),
            (TaskPersonalArcana2, "u"),
            (TaskPersonalArcana3, "v"),

            (TheMainTask40Years, "c"),
            (WhatBeforeYouTurn40Years, "c1"),
            (WhatAfterYouTurn40Years, "c2"),

            (WhatGivesYouMoney, "j"),
            (WhatOpensYourMoneyChannel, "l"),
            (AreasOfRealization, "c2"),

            (TasksOpenMoneyChannel1, "l"),
            (TasksOpenMoneyChannel2, "c2"),
            (WhatBlocksMoneyEnergy, "j"),
        ]

        with transaction.atomic():
            for Model, marker in model_marker_map:
                updated = 0
                for obj in Model.objects.all():
                    if not obj.marker:
                        obj.marker = marker
                        obj.save()
                        updated += 1
                self.stdout.write(
                    self.style.SUCCESS(
                        f"{Model.__name__}: обновлено {updated} записей (marker='{marker}')"
                    )
                )
#python manage.py assign_finance_markers
