from django.contrib import admin
from django.contrib.admin import AdminSite
from .models import (

    MatrixFateProgram,

    BirthTalent,
    YouthTalent,
    MatureTalent,
    Category,
    InnateTalent,
    QualitiesRevealed,
    QualitiesDeveloped,
    MainTask40,
    TaskBefore40,
    TaskAfter40,
    SoulComfortPoint,
    SelfRealization,
    SoulMainTask,
    PastLifeExperience,
    PastLifeLesson,
    PersonalPowerPoint,
    AncestralPower,
    TeachParents,
    RelationshipMistakes,
    PersonalGrowth,
    SpiritualTask1,
    SpiritualTask2,
    SpiritualTask3,
    PartnerTasks,
    SuitablePartner,
    MeetingPlace,
    RelationshipProblems,
    SuitableProfessions,
    MoneySources,
    MoneyGrowthTasks1,
    MoneyGrowthTasks2,
    MoneyBlocks,
    MoneyUnblock,
    PersonalPurpose1,
    PersonalPurpose2,
    PersonalPurpose3,
    SocialPurpose1,
    SocialPurpose2,
    SocialPurpose3,
    SpiritualPurpose,
    PaternalDiseases,
    MaternalDiseases,
    HealthArcane1,
    HealthArcane2,
    HealthArcane3,
    AncestralTaskFatherMale,
    AncestralTaskMotherMale,
    AncestralTaskFatherFemale,
    AncestralTaskMotherFemale,
    SahasraraO7,
    SahasraraP7,
    SahasraraQ7,
    AdjnaO6,
    AdjnaP6,
    AdjnaQ6,
    VishudkhaO5,
    VishudkhaP5,
    VishudkhaQ5,
    AnakhataO4,
    AnakhataP4,
    AnakhataQ4,
    ManipuraO3,
    ManipuraP3,
    ManipuraQ3,
    SvadkhistanaO2,
    SvadkhistanaP2,
    SvadkhistanaQ2,
    MuladkharaO1,
    MuladkharaP1,
    MuladkharaQ1,
    TotalO,
    TotalP,
    TotalQ,
)

#


class MatrixAdmin(AdminSite):
    site_header = "Управление данными для матрицы"
    site_title = "Админ панель Матрицы"
    index_title = "Добро пожаловать в админ панель Матрицы"

    def get_app_list(self, request):
        app_list = super().get_app_list(request)

        grouped_apps = [
            ("КАТЕГОРИИ", ["Category"]),
            ("ЛИЧНЫЕ КАЧЕСТВА", ["BirthTalent", "YouthTalent", "MatureTalent"]),
            (
                "КЕМ РАБОТАТЬ ДЛЯ ДУШИ",
                ["InnateTalent", "QualitiesRevealed", "QualitiesDeveloped"],
            ),
            ("КАРМА И ЗАДАЧА 40 ЛЕТ", ["MainTask40", "TaskBefore40", "TaskAfter40"]),
            ("ТОЧКА ДУШЕВНОГО КОМФОРТА", ["SoulComfortPoint"]),
            ("САМОРЕАЛИЗАЦИЯ", ["SelfRealization"]),
            (
                "ЗАДАЧИ КОТОРЫЕ ТЯНУТСЯ ИЗ ПРОШЛЫХ ЖИЗНЕЙ",
                ["SoulMainTask", "PastLifeExperience", "PastLifeLesson"],
            ),
            ("ТОЧКА ЛИЧНОЙ СИЛЫ", ["PersonalPowerPoint"]),
            ("СИЛА РОДА", ["AncestralPower"]),
            (
                "ДЕТСКО-РОДИТЕЛЬСКАЯ КАРМА",
                ["TeachParents", "RelationshipMistakes", "PersonalGrowth"],
            ),
            ("ДУХОВНАЯ КАРМА", ["SpiritualTask1", "SpiritualTask2", "SpiritualTask3"]),
            (
                "ОТНОШЕНИЯ В МАТРИЦЕ",
                [
                    "PartnerTasks",
                    "SuitablePartner",
                    "MeetingPlace",
                    "RelationshipProblems",
                ],
            ),
            (
                "ДЕНЬГИ В МАТРИЦЕ",
                [
                    "SuitableProfessions",
                    "MoneySources",
                    "MoneyGrowthTasks1",
                    "MoneyGrowthTasks2",
                    "MoneyBlocks",
                    "MoneyUnblock",
                ],
            ),
            (
                "ПРЕДНАЗНАЧЕНИЕ",
                [
                    "PersonalPurpose1",
                    "PersonalPurpose2",
                    "PersonalPurpose3",
                    "SocialPurpose1",
                    "SocialPurpose2",
                    "SocialPurpose3",
                    "SpiritualPurpose",
                ],
            ),
            (
                "ПРЕДРАСПОЛОЖЕННОСТЬ К ЗАБОЛЕВАНИЯМ",
                [
                    "PaternalDiseases",
                    "MaternalDiseases",
                    "HealthArcane1",
                    "HealthArcane2",
                    "HealthArcane3",
                ],
            ),
            (
                "ЗАДАЧИ РОДА ДО 7 КОЛЕНА",
                [
                    "AncestralTaskFatherMale",
                    "AncestralTaskMotherMale",
                    "AncestralTaskFatherFemale",
                    "AncestralTaskMotherFemale",
                ],
            ),
            (
                "КАРТА ЗДОРОВЬЯ",
                [
                    "SahasraraO7",
                    "SahasraraP7",
                    "SahasraraQ7",
                    "AdjnaO6",
                    "AdjnaP6",
                    "AdjnaQ6",
                    "VishudkhaO5",
                    "VishudkhaP5",
                    "VishudkhaQ5",
                    "AnakhataO4",
                    "AnakhataP4",
                    "AnakhataQ4",
                    "ManipuraO3",
                    "ManipuraP3",
                    "ManipuraQ3",
                    "SvadkhistanaO2",
                    "SvadkhistanaP2",
                    "SvadkhistanaQ2",
                    "MuladkharaO1",
                    "MuladkharaP1",
                    "MuladkharaQ1",
                    "TotalO",
                    "TotalP",
                    "TotalQ",
                ],

            ),
                ("ПРОГРАММЫ", ["MatrixFateProgram"]),
        ]

        grouped_models = {
            group[0]: {"name": group[0], "app_label": "", "models": []}
            for group in grouped_apps
        }

        for app in app_list:
            for model in app["models"]:
                model_name = model["object_name"]
                for group_name, model_names in grouped_apps:
                    if model_name in model_names:
                        grouped_models[group_name]["models"].append(model)

        new_app_list = [
            grouped_models[group_name]
            for group_name, _ in grouped_apps
            if grouped_models[group_name]["models"]
        ]

        return new_app_list


matrix_admin = MatrixAdmin(name="matrix_admin")


class BaseAdmin(admin.ModelAdmin):
    list_display = ("id", "order_id", "title", "description", "marker")
    search_fields = ("order_id", "title", "marker")
    list_filter = ("id",)
    list_per_page = 22
    list_display_links = ("order_id", "title", "description")


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "is_paid", "title", "description")
    search_fields = ("is_paid", "title")
    list_filter = ("is_paid",)
    list_display_links = ("is_paid", "title", "description")


class MatrixFateProgramAdmin(admin.ModelAdmin):
    list_display = (
        "id", "name", 
        "marker_1_name", "marker_1_value", 
        "marker_2_name", "marker_2_value", 
        "marker_3_name", "marker_3_value")
    search_fields = ("name",)
    list_filter = ("name",)


class BirthTalentAdmin(BaseAdmin):
    pass


class YouthTalentAdmin(BaseAdmin):
    pass


class MatureTalentAdmin(BaseAdmin):
    pass


class InnerTalentAdmin(BaseAdmin):
    pass


class QualitiesRevealedAdmin(BaseAdmin):
    pass


class QualitiesDevelopedAdmin(BaseAdmin):
    pass


class MainTask40Admin(BaseAdmin):
    pass


class TaskBefore40Admin(BaseAdmin):
    pass


class TaskAfter40Admin(BaseAdmin):
    pass


class SoulComfortPointAdmin(BaseAdmin):
    pass


class SelfRealizationAdmin(BaseAdmin):
    pass


class SoulMainTaskAdmin(BaseAdmin):
    pass


class PastLifeExperienceAdmin(BaseAdmin):
    pass


class PastLifeLessonAdmin(BaseAdmin):
    pass


class PersonalPowerPointAdmin(BaseAdmin):
    pass


class AncestralPowerAdmin(BaseAdmin):
    pass


class TeachParentsAdmin(BaseAdmin):
    pass


class RelationshipMistakesAdmin(BaseAdmin):
    pass


class PersonalGrowthAdmin(BaseAdmin):
    pass


class SpiritualTask1Admin(BaseAdmin):
    pass


class SpiritualTask2Admin(BaseAdmin):
    pass


class SpiritualTask3Admin(BaseAdmin):
    pass


class PartnerTasksAdmin(BaseAdmin):
    pass


class SuitablePartnerAdmin(BaseAdmin):
    pass


class MeetingPlaceAdmin(BaseAdmin):
    pass


class RelationshipProblemsAdmin(BaseAdmin):
    pass


class SuitableProfessionsAdmin(BaseAdmin):
    pass


class MoneySourcesAdmin(BaseAdmin):
    pass


class MoneyGrowthTasks1Admin(BaseAdmin):
    pass


class MoneyGrowthTasks2Admin(BaseAdmin):
    pass


class MoneyBlocksAdmin(BaseAdmin):
    pass


class MoneyUnblockAdmin(BaseAdmin):
    pass


class PersonalPurpose1Admin(BaseAdmin):
    pass


class PersonalPurpose2Admin(BaseAdmin):
    pass


class PersonalPurpose3Admin(BaseAdmin):
    pass


class SocialPurpose1Admin(BaseAdmin):
    pass


class SocialPurpose2Admin(BaseAdmin):
    pass


class SocialPurpose3Admin(BaseAdmin):
    pass


class SpiritualPurposeAdmin(BaseAdmin):
    pass


class PaternalDiseasesAdmin(BaseAdmin):
    pass


class MaternalDiseasesAdmin(BaseAdmin):
    pass


class HealthArcane1Admin(BaseAdmin):
    pass


class HealthArcane2Admin(BaseAdmin):
    pass


class HealthArcane3Admin(BaseAdmin):
    pass


class AncestralTaskFatherMaleAdmin(BaseAdmin):
    pass


class AncestralTaskMotherMaleAdmin(BaseAdmin):
    pass


class AncestralTaskFatherFemaleAdmin(BaseAdmin):
    pass


class AncestralTaskMotherFemaleAdmin(BaseAdmin):
    pass


class HealthMapAdmin(BaseAdmin):
    pass


class SahasraraO7Admin(BaseAdmin):
    pass


class SahasraraP7Admin(BaseAdmin):
    pass


class SahasraraQ7Admin(BaseAdmin):
    pass


class AdjnaO6Admin(BaseAdmin):
    pass


class AdjnaP6Admin(BaseAdmin):
    pass


class AdjnaQ6Admin(BaseAdmin):
    pass


class VishudkhaO5Admin(BaseAdmin):
    pass


class VishudkhaP5Admin(BaseAdmin):
    pass


class VishudkhaQ5Admin(BaseAdmin):
    pass


class AnakhataO4Admin(BaseAdmin):
    pass


class AnakhataP4Admin(BaseAdmin):
    pass


class AnakhataQ4Admin(BaseAdmin):
    pass


class ManipuraO3Admin(BaseAdmin):
    pass


class ManipuraP3Admin(BaseAdmin):
    pass


class ManipuraQ3Admin(BaseAdmin):
    pass


class SvadkhistanaO2Admin(BaseAdmin):
    pass


class SvadkhistanaP2Admin(BaseAdmin):
    pass


class SvadkhistanaQ2Admin(BaseAdmin):
    pass


class MuladkharaO1Admin(BaseAdmin):
    pass


class MuladkharaP1Admin(BaseAdmin):
    pass


class MuladkharaQ1Admin(BaseAdmin):
    pass


class TotalOAdmin(BaseAdmin):
    pass


class TotalPAdmin(BaseAdmin):
    pass


class TotalQAdmin(BaseAdmin):
    pass


matrix_admin.register(Category, CategoryAdmin)
matrix_admin.register(BirthTalent, BirthTalentAdmin)
matrix_admin.register(YouthTalent, YouthTalentAdmin)
matrix_admin.register(MatureTalent, MatureTalentAdmin)
matrix_admin.register(InnateTalent, InnerTalentAdmin)
matrix_admin.register(QualitiesRevealed, QualitiesRevealedAdmin)
matrix_admin.register(QualitiesDeveloped, QualitiesDevelopedAdmin)
matrix_admin.register(MainTask40, MainTask40Admin)
matrix_admin.register(TaskBefore40, TaskBefore40Admin)
matrix_admin.register(TaskAfter40, TaskAfter40Admin)
matrix_admin.register(SoulComfortPoint, SoulComfortPointAdmin)
matrix_admin.register(SelfRealization, SelfRealizationAdmin)
matrix_admin.register(SoulMainTask, SoulMainTaskAdmin)
matrix_admin.register(PastLifeExperience, PastLifeExperienceAdmin)
matrix_admin.register(PastLifeLesson, PastLifeLessonAdmin)
matrix_admin.register(PersonalPowerPoint, PersonalPowerPointAdmin)
matrix_admin.register(AncestralPower, AncestralPowerAdmin)
matrix_admin.register(TeachParents, TeachParentsAdmin)
matrix_admin.register(RelationshipMistakes, RelationshipMistakesAdmin)
matrix_admin.register(PersonalGrowth, PersonalGrowthAdmin)
matrix_admin.register(SpiritualTask1, SpiritualTask1Admin)
matrix_admin.register(SpiritualTask2, SpiritualTask2Admin)
matrix_admin.register(SpiritualTask3, SpiritualTask3Admin)
matrix_admin.register(PartnerTasks, PartnerTasksAdmin)
matrix_admin.register(SuitablePartner, SuitablePartnerAdmin)
matrix_admin.register(MeetingPlace, MeetingPlaceAdmin)
matrix_admin.register(RelationshipProblems, RelationshipProblemsAdmin)
matrix_admin.register(SuitableProfessions, SuitableProfessionsAdmin)
matrix_admin.register(MoneySources, MoneySourcesAdmin)
matrix_admin.register(MoneyGrowthTasks1, MoneyGrowthTasks1Admin)
matrix_admin.register(MoneyGrowthTasks2, MoneyGrowthTasks2Admin)
matrix_admin.register(MoneyBlocks, MoneyBlocksAdmin)
matrix_admin.register(MoneyUnblock, MoneyUnblockAdmin)
matrix_admin.register(PersonalPurpose1, PersonalPurpose1Admin)
matrix_admin.register(PersonalPurpose2, PersonalPurpose2Admin)
matrix_admin.register(PersonalPurpose3, PersonalPurpose3Admin)
matrix_admin.register(SocialPurpose1, SocialPurpose1Admin)
matrix_admin.register(SocialPurpose2, SocialPurpose2Admin)
matrix_admin.register(SocialPurpose3, SocialPurpose3Admin)
matrix_admin.register(SpiritualPurpose, SpiritualPurposeAdmin)
matrix_admin.register(PaternalDiseases, PaternalDiseasesAdmin)
matrix_admin.register(MaternalDiseases, MaternalDiseasesAdmin)
matrix_admin.register(HealthArcane1, HealthArcane1Admin)
matrix_admin.register(HealthArcane2, HealthArcane2Admin)
matrix_admin.register(HealthArcane3, HealthArcane3Admin)
matrix_admin.register(AncestralTaskFatherMale, AncestralTaskFatherMaleAdmin)
matrix_admin.register(AncestralTaskMotherMale, AncestralTaskMotherMaleAdmin)
matrix_admin.register(AncestralTaskFatherFemale, AncestralTaskFatherFemaleAdmin)
matrix_admin.register(AncestralTaskMotherFemale, AncestralTaskMotherFemaleAdmin)
matrix_admin.register(SahasraraO7, SahasraraO7Admin)
matrix_admin.register(SahasraraP7, SahasraraP7Admin)
matrix_admin.register(SahasraraQ7, SahasraraQ7Admin)
matrix_admin.register(AdjnaO6, AdjnaO6Admin)
matrix_admin.register(AdjnaP6, AdjnaP6Admin)
matrix_admin.register(AdjnaQ6, AdjnaQ6Admin)
matrix_admin.register(VishudkhaO5, VishudkhaO5Admin)
matrix_admin.register(VishudkhaP5, VishudkhaP5Admin)
matrix_admin.register(VishudkhaQ5, VishudkhaQ5Admin)
matrix_admin.register(AnakhataO4, AnakhataO4Admin)
matrix_admin.register(AnakhataP4, AnakhataP4Admin)
matrix_admin.register(AnakhataQ4, AnakhataQ4Admin)
matrix_admin.register(ManipuraO3, ManipuraO3Admin)
matrix_admin.register(ManipuraP3, ManipuraP3Admin)
matrix_admin.register(ManipuraQ3, ManipuraQ3Admin)
matrix_admin.register(SvadkhistanaO2, SvadkhistanaO2Admin)
matrix_admin.register(SvadkhistanaP2, SvadkhistanaP2Admin)
matrix_admin.register(SvadkhistanaQ2, SvadkhistanaQ2Admin)
matrix_admin.register(MuladkharaO1, MuladkharaO1Admin)
matrix_admin.register(MuladkharaP1, MuladkharaP1Admin)
matrix_admin.register(MuladkharaQ1, MuladkharaQ1Admin)
matrix_admin.register(TotalO, TotalOAdmin)
matrix_admin.register(TotalP, TotalPAdmin)
matrix_admin.register(TotalQ, TotalQAdmin)
matrix_admin.register(MatrixFateProgram, MatrixFateProgramAdmin)
