from django.contrib import admin
from django.contrib.admin import AdminSite
from .models import (
    FinanceCategory,
    YourGreatestTalentBirth,
    QualitiesRevealedAge20,
    QualitiesDevelopAge40,
    YourOpportunity,
    TaskPersonalArcana1,
    TaskPersonalArcana2,
    TaskPersonalArcana3,
    WhatGivesYouMoney,
    WhatOpensYourMoneyChannel,
    AreasOfRealization,
    TasksOpenMoneyChannel1,
    TasksOpenMoneyChannel2,
    WhatBlocksMoneyEnergy,
    TheMainTask40Years,
    WhatBeforeYouTurn40Years,
    WhatAfterYouTurn40Years,
    MatrixFinanceProgram
)


class MatrixAdmin(AdminSite):
    site_header = "Управление данными для матрицы финансов"
    site_title = "Админ панель Матрицы Финансов"
    index_title = "Добро пожаловать в админ панель Матрицы Финансов"

    def get_app_list(self, request):
        """Группировка и строгая сортировка моделей в админке"""
        app_list = super().get_app_list(request)

        grouped_apps = [
            ("КАТЕГОРИИ", ["FinanceCategory"]),
            (
                "ТАЛАНТЫ",
                [
                    "YourGreatestTalentBirth",
                    "QualitiesRevealedAge20",
                    "QualitiesDevelopAge40",
                ],
            ),
            ("САМОРЕАЛИЗАЦИЯ", ["YourOpportunity"]),
            (
                "ПРЕДНАЗНАЧЕНИЕ ДЛЯ СОЦИУМА",
                ["TaskPersonalArcana1", "TaskPersonalArcana2", "TaskPersonalArcana3"],
            ),
            (
                "КАРМА И ЗАДАЧА 40 ЛЕТ",
                [
                    "TheMainTask40Years",
                    "WhatBeforeYouTurn40Years",
                    "WhatAfterYouTurn40Years",
                ],
            ),
            (
                "ЧТО ДАЕТ ДЕНЬГИ",
                [
                    "WhatGivesYouMoney",
                    "WhatOpensYourMoneyChannel",
                    "AreasOfRealization",
                ],
            ),
            (
                "ЧТО БЛОКИРУЕТ ДЕНЕЖНУЮ ЭНЕРГИЮ",
                [
                    "TasksOpenMoneyChannel1",
                    "TasksOpenMoneyChannel2",
                    "WhatBlocksMoneyEnergy",
                ],
            ),

            ("ПРОГРАММЫ", ["MatrixFinanceProgram"]),
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


finance_admin = MatrixAdmin(name="finance_admin")


class BaseAdmin(admin.ModelAdmin):
    list_display = ("id", "order_id", "title", "description", "marker")
    search_fields = ("order_id", "title", "marker")
    list_filter = ("id",)
    list_per_page = 22
    list_display_links = ("order_id", "title", "description")


class FinanceCategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "is_paid", "title", "description")
    search_fields = ("is_paid", "title")
    list_filter = ("is_paid",)
    list_display_links = ("is_paid", "title", "description")

class MatrixFinanceProgramAdmin(admin.ModelAdmin):
    list_display = (
        "id", "name", 
        "marker_1_name", "marker_1_value", 
        "marker_2_name", "marker_2_value", 
        "marker_3_name", "marker_3_value")
    search_fields = ("name",)
    list_filter = ("name",)


class YourGreatestTalentBirthAdmin(BaseAdmin):
    pass


class QualitiesRevealedAge20Admin(BaseAdmin):
    pass


class QualitiesDevelopAge40Admin(BaseAdmin):
    pass


class YourOpportunityAdmin(BaseAdmin):
    pass


class TaskPersonalArcana1Admin(BaseAdmin):
    pass


class TaskPersonalArcana2Admin(BaseAdmin):
    pass


class TaskPersonalArcana3Admin(BaseAdmin):
    pass


class WhatGivesYouMoneyAdmin(BaseAdmin):
    pass


class WhatOpensYourMoneyChannelAdmin(BaseAdmin):
    pass


class AreasOfRealizationAdmin(BaseAdmin):
    pass


class TasksOpenMoneyChannel1Admin(BaseAdmin):
    pass


class TasksOpenMoneyChannel2Admin(BaseAdmin):
    pass


class WhatBlocksMoneyEnergyAdmin(BaseAdmin):
    pass

class TheMainTask40YearsAdmin(BaseAdmin):
    pass

class WhatBeforeYouTurn40YearsAdmin(BaseAdmin):
    pass

class WhatAfterYouTurn40YearsAdmin(BaseAdmin):
    pass


finance_admin.register(FinanceCategory, FinanceCategoryAdmin)
finance_admin.register(YourGreatestTalentBirth, YourGreatestTalentBirthAdmin)
finance_admin.register(QualitiesRevealedAge20, QualitiesRevealedAge20Admin)
finance_admin.register(QualitiesDevelopAge40, QualitiesDevelopAge40Admin)
finance_admin.register(YourOpportunity, YourOpportunityAdmin)
finance_admin.register(TaskPersonalArcana1, TaskPersonalArcana1Admin)
finance_admin.register(TaskPersonalArcana2, TaskPersonalArcana2Admin)
finance_admin.register(TaskPersonalArcana3, TaskPersonalArcana3Admin)
finance_admin.register(WhatGivesYouMoney, WhatGivesYouMoneyAdmin)
finance_admin.register(WhatOpensYourMoneyChannel, WhatOpensYourMoneyChannelAdmin)
finance_admin.register(AreasOfRealization, AreasOfRealizationAdmin)
finance_admin.register(TasksOpenMoneyChannel1, TasksOpenMoneyChannel1Admin)
finance_admin.register(TasksOpenMoneyChannel2, TasksOpenMoneyChannel2Admin)
finance_admin.register(WhatBlocksMoneyEnergy, WhatBlocksMoneyEnergyAdmin)
finance_admin.register(TheMainTask40Years, TheMainTask40YearsAdmin)
finance_admin.register(WhatBeforeYouTurn40Years, WhatBeforeYouTurn40YearsAdmin)
finance_admin.register(WhatAfterYouTurn40Years, WhatAfterYouTurn40YearsAdmin)
finance_admin.register(MatrixFinanceProgram, MatrixFinanceProgramAdmin)
