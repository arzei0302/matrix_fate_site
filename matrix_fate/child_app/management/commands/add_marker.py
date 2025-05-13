# from django.core.management.base import BaseCommand
# # from child_app.models import ChildOpportunity
# # from matrix_fate.child_app.models import ChildOpportunity
# from matrix_fate.child_app.models import ChildBusinessCard

# from django.db.models import Q

# class Command(BaseCommand):
#     help = "Устанавливает marker='a' для всех ChildOpportunity без маркера"

#     def handle(self, *args, **options):
#         updated = ChildBusinessCard.objects.filter(
#             Q(marker__isnull=True) | Q(marker="")
#         ).update(marker="a")
#         self.stdout.write(self.style.SUCCESS(f"Обновлено записей: {updated}"))

# #python manage.py add_marker

from django.core.management.base import BaseCommand
from django.db.models import Q

from matrix_fate.child_app.models import (
    QualitiesRevealedAgeOf20, ThirdTalentRevealedAge40,
    ChildPointOfComfort, MainTaskSoul, SoulPastExperiencesWithPeople,
    LessonsFromPastLife, ChildDestinyArcana1, ChildDestinyArcana2, ChildDestinyArcana3,
    WhatChildShouldTeachParents, WhatMistakesRelationshipParentsChildren, WhatShouldComeQualitiesChild,
)


class Command(BaseCommand):
    help = "Устанавливает marker для нескольких моделей по заранее заданному словарю"

    MODEL_MARKER_MAP = {
        QualitiesRevealedAgeOf20: "b",
        ThirdTalentRevealedAge40: "c",
        ChildPointOfComfort: "e",
        MainTaskSoul: "d",
        SoulPastExperiencesWithPeople: "d2",
        LessonsFromPastLife: "d1",
        ChildDestinyArcana1: "r",
        ChildDestinyArcana2: "s",
        ChildDestinyArcana3: "y",
        WhatChildShouldTeachParents: "a",
        WhatMistakesRelationshipParentsChildren: "a2",
        WhatShouldComeQualitiesChild: "a1",
    }

    def handle(self, *args, **options):
        for model_class, marker_value in self.MODEL_MARKER_MAP.items():
            model_name = model_class.__name__

            if not hasattr(model_class, "marker"):
                self.stdout.write(self.style.WARNING(
                    f"Модель '{model_name}' не содержит поле 'marker' — пропущена."))
                continue

            updated = model_class.objects.filter(
                Q(marker__isnull=True) | Q(marker="")
            ).update(marker=marker_value)

            self.stdout.write(self.style.SUCCESS(
                f"Модель '{model_name}': обновлено {updated} объектов (marker='{marker_value}')"
            ))

