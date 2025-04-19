from django.core.management.base import BaseCommand
from matrix_fate_app.models import (
    BirthTalent, YouthTalent, MatureTalent,
    InnateTalent, QualitiesRevealed, QualitiesDeveloped,
    MainTask40, TaskBefore40, TaskAfter40,
    SoulComfortPoint,
    SelfRealization,
    SoulMainTask, PastLifeExperience, PastLifeLesson,
    PersonalPowerPoint,
    AncestralPower,
    TeachParents, RelationshipMistakes, PersonalGrowth,
    SpiritualTask1, SpiritualTask2, SpiritualTask3,
    PartnerTasks, SuitablePartner, MeetingPlace, RelationshipProblems,

    SuitableProfessions, MoneySources, MoneyGrowthTasks1, MoneyGrowthTasks2, 
    MoneyBlocks, MoneyUnblock,

    PersonalPurpose1, PersonalPurpose2, PersonalPurpose3, SocialPurpose1, 
    SocialPurpose2, SocialPurpose3, SpiritualPurpose,

    PaternalDiseases, MaternalDiseases, HealthArcane1, HealthArcane2, HealthArcane3,
    AncestralTaskFatherFemale, AncestralTaskMotherFemale, AncestralTaskFatherMale, AncestralTaskMotherMale,

    SahasraraO7, SahasraraP7, SahasraraQ7,
    AdjnaO6, AdjnaP6, AdjnaQ6,
    VishudkhaO5, VishudkhaP5, VishudkhaQ5,
    AnakhataO4, AnakhataP4, AnakhataQ4,
    ManipuraO3, ManipuraP3, ManipuraQ3,
    SvadkhistanaO2, SvadkhistanaP2, SvadkhistanaQ2,
    MuladkharaO1, MuladkharaP1, MuladkharaQ1,
    TotalO, TotalP, TotalQ,
)
from django.db import transaction


class Command(BaseCommand):
    help = "Назначает маркеры (a, b, c и т.д.) объектам с order_id"

    def handle(self, *args, **options):
        # Сопоставление: (модель, маркер)
        model_marker_map = [
            (BirthTalent, "a"),
            (YouthTalent, "b"),
            (MatureTalent, "c"),

            (InnateTalent, "a"),
            (QualitiesRevealed, "b"),
            (QualitiesDeveloped, "c"),

            (MainTask40, "d"),
            (TaskBefore40, "d1"),
            (TaskAfter40, "d2"),

            (SoulComfortPoint, "e"),
            
            (SelfRealization, "a2"),

            (SoulMainTask,  "d"),
            (PastLifeExperience, "d2"),
            (PastLifeLesson, "d1"),

            (PersonalPowerPoint, "e"),

            (AncestralPower, "e1"),

            (TeachParents,  "a"),
            (RelationshipMistakes, "a2"),
            (PersonalGrowth, "a1"),

            (SpiritualTask1, "b"),
            (SpiritualTask2, "b1"),
            (SpiritualTask3, "b2"),

            (PartnerTasks, "d2"),
            (SuitablePartner, "k"),
            (MeetingPlace, "k"),
            (RelationshipProblems, "j"),

            (SuitableProfessions, "c2"),
            (MoneySources, "l"),
            (MoneyGrowthTasks1, "l"),
            (MoneyGrowthTasks2, "c2"),
            (MoneyBlocks, "j"),
            (MoneyUnblock, "j"),

            (PersonalPurpose1, "r"),
            (PersonalPurpose2, "s"),
            (PersonalPurpose3, "y"),
            (SocialPurpose1, "t"),
            (SocialPurpose2, "u"),
            (SocialPurpose3, "v"),
            (SpiritualPurpose, "w"),

            (PaternalDiseases, "h"),
            (MaternalDiseases, "i"),
            (HealthArcane1, "a"),
            (HealthArcane2, "b"),
            (HealthArcane3, "c"),

            (AncestralTaskFatherMale, "f"),
            (AncestralTaskMotherMale, "h"),
            (AncestralTaskFatherFemale, "g"),
            (AncestralTaskMotherFemale, "i"),

            (SahasraraO7, "o7"),
            (SahasraraP7, "p7"),
            (SahasraraQ7, "q7"),

            (AdjnaO6, "o6"),
            (AdjnaP6, "p6"),
            (AdjnaQ6, "q6"),

            (VishudkhaO5, "o5"),
            (VishudkhaP5, "p5"),
            (VishudkhaQ5, "q5"),

            (AnakhataO4, "o4"),
            (AnakhataP4, "p4"),
            (AnakhataQ4, "q4"),

            (ManipuraO3, "o3"),
            (ManipuraP3, "p3"),
            (ManipuraQ3, "q3"),

            (SvadkhistanaO2, "o2"),
            (SvadkhistanaP2, "p2"),
            (SvadkhistanaQ2, "q2"),

            (MuladkharaO1, "o1"),
            (MuladkharaP1, "p1"),
            (MuladkharaQ1, "q1"),

            (TotalO, "o"),
            (TotalP, "p"),
            (TotalQ, "q"),


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
#python manage.py assign_markers
