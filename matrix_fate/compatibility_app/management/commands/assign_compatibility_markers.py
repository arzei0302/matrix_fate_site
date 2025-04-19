from django.core.management.base import BaseCommand
from django.db import transaction
from compatibility_app.models import(
    WhyDidYouMeet,
    TasksForCoupleArcana1, TasksForCoupleArcana2, TasksForCoupleArcana3,
    CoupleResourcesArcana1, CoupleResourcesArcana2,
    WhatFillsTheVapor,
    CouplesTaskForSociety,
    WhatGivesTribute, WhatTasksUnlockMoneyChannels, WhatBlocksMonetaryEnergy,
    CoupleRelations1, CoupleRelations2, WhatRelationshipProblemsCanArise,
)


class Command(BaseCommand):
    help = "Назначает маркеры (a, b, c и т.д.) объектам с order_id"

    def handle(self, *args, **options):
        model_marker_map = [
            (WhyDidYouMeet, "a"),

            (TasksForCoupleArcana1, "w"),
            (TasksForCoupleArcana2, "d"),
            (TasksForCoupleArcana3, "y"),

            (CoupleResourcesArcana1, "b"),
            (CoupleResourcesArcana2, "c"),

            (WhatFillsTheVapor, "e"),

            (CouplesTaskForSociety, "v"),

            (WhatGivesTribute, "c2"),
            (WhatTasksUnlockMoneyChannels, "l"),
            (WhatBlocksMonetaryEnergy, "j"),

            (CoupleRelations1, "d2"),
            (CoupleRelations2, "k"),
            (WhatRelationshipProblemsCanArise, "j"),
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
#python manage.py assign_compatibility_markers
