from django.contrib import admin
from django.contrib.admin import AdminSite
from .models import (
    ChildCategory,
    ChildBusinessCard,
    QualitiesRevealedAgeOf20,
    ThirdTalentRevealedAge40,
    ChildOpportunity,
    ChildPointOfComfort,
    MainTaskSoul,
    SoulPastExperiencesWithPeople,
    LessonsFromPastLife,
    ChildDestinyArcana1,
    ChildDestinyArcana2,
    ChildDestinyArcana3,
    WhatChildShouldTeachParents,
    WhatMistakesRelationshipParentsChildren,
    WhatShouldComeQualitiesChild,
    MatrixChildProgram,
)


class MatrixAdmin(AdminSite):
    site_header = "Управление данными для Детской матрицы"
    site_title = "Админ панель Детской матрицы"
    index_title = "Добро пожаловать в админ панель Детской матрицы"

    def get_app_list(self, request):
        """Группировка и строгая сортировка моделей в админке"""
        app_list = super().get_app_list(request)

        grouped_apps = [
            ("Категории", 
                ["ChildCategory"]
                ),
            ("Главный талант ребенка от рождения", 
                ["ChildBusinessCard"]
                ),
            ("Личные качества",
                ["QualitiesRevealedAgeOf20", "ThirdTalentRevealedAge40"]
            ),
            ("Самореализация ребенка", 
                ["ChildOpportunity"]
                ),
            ("Точка душевного комфорта ребенка", 
             ["ChildPointOfComfort"]
             ),
            ("Задачи, которые тянутся из прошлых жизней",
                ["MainTaskSoul",
                "SoulPastExperiencesWithPeople",
                "LessonsFromPastLife"]
            ),
            ("Предназначение ребенка",
                ["ChildDestinyArcana1", "ChildDestinyArcana2", "ChildDestinyArcana3"]
            ),
            ("Детско-родительская карма",
                ["WhatChildShouldTeachParents",
                "WhatMistakesRelationshipParentsChildren",
                "WhatShouldComeQualitiesChild"]
            ),
            (" Программы", 
                ["MatrixChildProgram"]
                ),
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


child_admin = MatrixAdmin(name="child_admin")


class BaseAdmin(admin.ModelAdmin):
    list_display = ("id", "order_id", "title", "description", "marker")
    search_fields = ("order_id", "title", "marker")
    list_filter = ("id",)
    list_per_page = 22
    list_display_links = ("order_id", "title", "description")
    readonly_fields = ("order_id", "marker")


class ChildCategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "is_paid", "title", "description")
    search_fields = ("is_paid", "title")
    list_filter = ("is_paid",)
    list_display_links = ("is_paid", "title", "description")


class MatrixChildProgramAdmin(admin.ModelAdmin):
    list_display = (
        "id", "name", 
        "marker_1_name", "marker_1_value", 
        "marker_2_name", "marker_2_value", 
        "marker_3_name", "marker_3_value",
        "is_paid")
    search_fields = ("name",)
    list_filter = ("name", "is_paid")


class ChildBusinessCardAdmin(BaseAdmin):
    pass

class QualitiesRevealedAgeOf20Admin(BaseAdmin):
    pass

class ThirdTalentRevealedAge40Admin(BaseAdmin):
    pass

class ChildOpportunityAdmin(BaseAdmin):
    pass

class ChildPointOfComfortAdmin(BaseAdmin):
    pass

class MainTaskSoulAdmin(BaseAdmin):
    pass

class SoulPastExperiencesWithPeopleAdmin(BaseAdmin):
    pass

class LessonsFromPastLifeAdmin(BaseAdmin):
    pass

class ChildDestinyArcana1Admin(BaseAdmin):
    pass

class ChildDestinyArcana2Admin(BaseAdmin):
    pass

class ChildDestinyArcana3Admin(BaseAdmin):
    pass

class WhatChildShouldTeachParentsAdmin(BaseAdmin):
    pass

class WhatMistakesRelationshipParentsChildrenAdmin(BaseAdmin):
    pass

class WhatShouldComeQualitiesChildAdmin(BaseAdmin):
    pass


child_admin.register(ChildCategory, ChildCategoryAdmin)
child_admin.register(ChildBusinessCard, ChildBusinessCardAdmin)
child_admin.register(QualitiesRevealedAgeOf20, QualitiesRevealedAgeOf20Admin)
child_admin.register(ThirdTalentRevealedAge40, ThirdTalentRevealedAge40Admin)
child_admin.register(ChildOpportunity, ChildOpportunityAdmin)
child_admin.register(ChildPointOfComfort, ChildPointOfComfortAdmin)
child_admin.register(MainTaskSoul, MainTaskSoulAdmin)
child_admin.register(SoulPastExperiencesWithPeople, SoulPastExperiencesWithPeopleAdmin)
child_admin.register(LessonsFromPastLife, LessonsFromPastLifeAdmin)
child_admin.register(ChildDestinyArcana1, ChildDestinyArcana1Admin)
child_admin.register(ChildDestinyArcana2, ChildDestinyArcana2Admin)
child_admin.register(ChildDestinyArcana3, ChildDestinyArcana3Admin)
child_admin.register(WhatChildShouldTeachParents, WhatChildShouldTeachParentsAdmin)
child_admin.register(WhatMistakesRelationshipParentsChildren, WhatMistakesRelationshipParentsChildrenAdmin)
child_admin.register(WhatShouldComeQualitiesChild, WhatShouldComeQualitiesChildAdmin)
child_admin.register(MatrixChildProgram, MatrixChildProgramAdmin)