from django.core.management.base import BaseCommand
from django.db import transaction
from child_app.models import (
    ChildBusinessCard,
    QualitiesRevealedAgeOf20, ThirdTalentRevealedAge40,
    ChildOpportunity,
    ChildPointOfComfort,
    MainTaskSoul, SoulPastExperiencesWithPeople, LessonsFromPastLife,
    ChildDestinyArcana1, ChildDestinyArcana2, ChildDestinyArcana3,
    WhatChildShouldTeachParents, WhatMistakesRelationshipParentsChildren, WhatShouldComeQualitiesChild,
)


class Command(BaseCommand):
    help = "Назначает маркеры (a, b, c и т.д.) объектам с order_id"

    def handle(self, *args, **options):
        model_marker_map = [
            (ChildBusinessCard, "a"),

            (QualitiesRevealedAgeOf20, "b"),
            (ThirdTalentRevealedAge40, "c"),

            (ChildOpportunity, "a2"),

            (ChildPointOfComfort, "e"),

            (MainTaskSoul, "d"),
            (SoulPastExperiencesWithPeople, "d2"),
            (LessonsFromPastLife, "d1"),

            (ChildDestinyArcana1, "r"),
            (ChildDestinyArcana2, "s"),
            (ChildDestinyArcana3, "y"),

            (WhatChildShouldTeachParents, "a"),
            (WhatMistakesRelationshipParentsChildren, "a2"),
            (WhatShouldComeQualitiesChild, "a1"),
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
#python manage.py assign_child_markers
