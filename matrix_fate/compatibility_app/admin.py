from django.contrib import admin
from django.contrib.admin import AdminSite
from .models import (
    CompatibilityCategory,
    WhyDidYouMeet,
    TasksForCoupleArcana1,
    TasksForCoupleArcana2,
    TasksForCoupleArcana3,
    CoupleResourcesArcana1,
    CoupleResourcesArcana2,
    WhatFillsTheVapor,
    CouplesTaskForSociety,
    WhatGivesTribute,
    WhatTasksUnlockMoneyChannels,
    WhatBlocksMonetaryEnergy,
    CoupleRelations1,
    CoupleRelations2,
    WhatRelationshipProblemsCanArise,
    MatrixCompatibilityProgram
)


class MatrixAdmin(AdminSite):
    site_header = "Управление данными для матрицы совместимости"
    site_title = "Админ панель Матрицы Совместимости"
    index_title = "Добро пожаловать в админ панель Матрицы Совместимости"

    def get_app_list(self, request):
        """Группировка и строгая сортировка моделей в админке"""
        app_list = super().get_app_list(request)

        grouped_apps = [
            ("Категории", ["CompatibilityCategory"]),
            ("Для чего вы встретились", ["WhyDidYouMeet"]),
            (
                "Задачи для пары",
                [
                    "TasksForCoupleArcana1",
                    "TasksForCoupleArcana2",
                    "TasksForCoupleArcana3",
                ],
            ),
            ("Ресурсы пары", ["CoupleResourcesArcana1", "CoupleResourcesArcana2"]),
            ("От чего наполняется пара", ["WhatFillsTheVapor"]),
            ("Задача пары для социума", ["CouplesTaskForSociety"]),
            (
                "Деньги в паре",
                [
                    "WhatGivesTribute",
                    "WhatTasksUnlockMoneyChannels",
                    "WhatBlocksMonetaryEnergy",
                ],
            ),
            (
                "Отношения в паре",
                [
                    "CoupleRelations1",
                    "CoupleRelations2",
                    "WhatRelationshipProblemsCanArise",
                ],
            ),

            ("ПРОГРАММЫ", ["MatrixCompatibilityProgram"]),

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


compatibility_admin = MatrixAdmin(name="compatibility_admin")


class BaseAdmin(admin.ModelAdmin):
    list_display = ("id", "order_id", "title", "description", "marker")
    search_fields = ("order_id", "title", "marker")
    list_filter = ("id",)
    list_per_page = 22
    list_display_links = ("order_id", "title", "description")


class CompatibilityCategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "is_paid", "title", "description")
    search_fields = ("is_paid", "title")
    list_filter = ("is_paid",)
    list_display_links = ("is_paid", "title", "description")


class MatrixCompatibilityProgramAdmin(admin.ModelAdmin):
    list_display = (
        "id", "name", 
        "marker_1_name", "marker_1_value", 
        "marker_2_name", "marker_2_value", 
        "marker_3_name", "marker_3_value",
        "is_paid")
    search_fields = ("name",)
    list_filter = ("name", "is_paid")


class WhyDidYouMeetAdmin(BaseAdmin):
    pass


class TasksForCoupleArcana1Admin(BaseAdmin):
    pass


class TasksForCoupleArcana2Admin(BaseAdmin):
    pass


class TasksForCoupleArcana3Admin(BaseAdmin):
    pass


class CoupleResourcesArcana1Admin(BaseAdmin):
    pass


class CoupleResourcesArcana2Admin(BaseAdmin):
    pass


class WhatFillsTheVaporAdmin(BaseAdmin):
    pass


class CouplesTaskForSocietyAdmin(BaseAdmin):
    pass


class WhatGivesTributeAdmin(BaseAdmin):
    pass


class WhatTasksUnlockMoneyChannelsAdmin(BaseAdmin):
    pass


class WhatBlocksMonetaryEnergyAdmin(BaseAdmin):
    pass


class CoupleRelations1Admin(BaseAdmin):
    pass


class CoupleRelations2Admin(BaseAdmin):
    pass


class WhatRelationshipProblemsCanAriseAdmin(BaseAdmin):
    pass


compatibility_admin.register(CompatibilityCategory, CompatibilityCategoryAdmin)
compatibility_admin.register(WhyDidYouMeet, WhyDidYouMeetAdmin)
compatibility_admin.register(TasksForCoupleArcana1, TasksForCoupleArcana1Admin)
compatibility_admin.register(TasksForCoupleArcana2, TasksForCoupleArcana2Admin)
compatibility_admin.register(TasksForCoupleArcana3, TasksForCoupleArcana3Admin)
compatibility_admin.register(CoupleResourcesArcana1, CoupleResourcesArcana1Admin)
compatibility_admin.register(CoupleResourcesArcana2, CoupleResourcesArcana2Admin)
compatibility_admin.register(WhatFillsTheVapor, WhatFillsTheVaporAdmin)
compatibility_admin.register(CouplesTaskForSociety, CouplesTaskForSocietyAdmin)
compatibility_admin.register(WhatGivesTribute, WhatGivesTributeAdmin)
compatibility_admin.register(
    WhatTasksUnlockMoneyChannels, WhatTasksUnlockMoneyChannelsAdmin
)
compatibility_admin.register(WhatBlocksMonetaryEnergy, WhatBlocksMonetaryEnergyAdmin)
compatibility_admin.register(CoupleRelations1, CoupleRelations1Admin)
compatibility_admin.register(CoupleRelations2, CoupleRelations2Admin)
compatibility_admin.register(
    WhatRelationshipProblemsCanArise, WhatRelationshipProblemsCanAriseAdmin
)
compatibility_admin.register(MatrixCompatibilityProgram, MatrixCompatibilityProgramAdmin)
