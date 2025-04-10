# from django.core.management.base import BaseCommand
# from django.utils.html import escape
# from child_app.models import (
#     ChildCategory,
#     ChildBusinessCard,
#     QualitiesRevealedAgeOf20,
#     ThirdTalentRevealedAge40,
#     ChildOpportunity,
#     ChildPointOfComfort,
#     MainTaskSoul,
#     SoulPastExperiencesWithPeople,
#     LessonsFromPastLife,
#     ChildDestinyArcana1,
#     ChildDestinyArcana2,
#     ChildDestinyArcana3,
#     WhatChildShouldTeachParents,
#     WhatMistakesRelationshipParentsChildren,
#     WhatShouldComeQualitiesChild,
# )

# CATEGORY_MAPPING = {
#     "Главный талант ребенка от рождения": 1,
#     "Личные качества": 2,
#     "Самореализация ребенка": 3,
#     "Точка душевного комфорта ребенка": 4,
#     "Задачи, которые тянутся из прошлых жизней": 5,
#     "Предназначение ребенка": 6,
#     "Детско-родительская карма": 7,
# }

# def create_entries(model, category_id, title_prefix, description_prefix):
#     category = ChildCategory.objects.get(id=category_id)
#     entries = [
#         model(
#             category=category,
#             title=f"{title_prefix} {i}",
#             description=escape(f"{description_prefix} {i}"),
#             order_id=i,
#         ) for i in range(1, 23)
#     ]
#     model.objects.bulk_create(entries)

# class Command(BaseCommand):
#     help = "Заполняет таблицы данными"

#     def handle(self, *args, **kwargs):
#         create_entries(ChildBusinessCard, CATEGORY_MAPPING["Главный талант ребенка от рождения"], "Главный талант ребенка от рождения", "Главный талант ребенка от рождения")

#         create_entries(QualitiesRevealedAgeOf20, CATEGORY_MAPPING["Личные качества"], "Личные качества", "Личные качества")
#         create_entries(ThirdTalentRevealedAge40, CATEGORY_MAPPING["Личные качества"], "Личные качества", "Личные качества")

#         create_entries(ChildOpportunity, CATEGORY_MAPPING["Самореализация ребенка"], "Самореализация ребенка", "Самореализация ребенка")
        
#         create_entries(ChildPointOfComfort, CATEGORY_MAPPING["Точка душевного комфорта ребенка"], "Точка душевного комфорта ребенка", "Точка душевного комфорта ребенка")

#         create_entries(MainTaskSoul, CATEGORY_MAPPING["Задачи, которые тянутся из прошлых жизней"], "Задачи, из прошлых жизней", "Задачи, из прошлых жизней")
#         create_entries(SoulPastExperiencesWithPeople, CATEGORY_MAPPING["Задачи, которые тянутся из прошлых жизней"], "Задачи, из прошлых жизней", "Задачи, из прошлых жизней")
#         create_entries(LessonsFromPastLife, CATEGORY_MAPPING["Задачи, которые тянутся из прошлых жизней"], "Задачи, из прошлых жизней", "Задачи, из прошлых жизней")

#         create_entries(ChildDestinyArcana1, CATEGORY_MAPPING["Предназначение ребенка"], "Предназначение ребенка", "Предназначение ребенка")
#         create_entries(ChildDestinyArcana2, CATEGORY_MAPPING["Предназначение ребенка"], "Предназначение ребенка", "Предназначение ребенка")
#         create_entries(ChildDestinyArcana3, CATEGORY_MAPPING["Предназначение ребенка"], "Предназначение ребенка", "Предназначение ребенка")

#         create_entries(WhatChildShouldTeachParents, CATEGORY_MAPPING["Отношения в паре"], "Отношения в паре", "Отношения в паре")
#         create_entries(WhatMistakesRelationshipParentsChildren, CATEGORY_MAPPING["Отношения в паре"], "Отношения в паре", "Отношения в паре")
#         create_entries(WhatShouldComeQualitiesChild, CATEGORY_MAPPING["Отношения в паре"], "Отношения в паре", "Отношения в паре")
        
#         self.stdout.write(self.style.SUCCESS("База данных успешно заполнена 22 записями в каждую таблицу!"))


# # python manage.py fill_child_data

from django.core.management.base import BaseCommand
from django.utils.html import escape
from child_app.models import (
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
)

CATEGORY_MAPPING = {
    "Главный талант ребенка от рождения": 1,
    "Личные качества": 2,
    "Самореализация ребенка": 3,
    "Точка душевного комфорта ребенка": 4,
    "Задачи, которые тянутся из прошлых жизней": 5,
    "Предназначение ребенка": 6,
    "Детско-родительская карма": 7,
}

MODELS_MAPPING = {
    "Главный талант ребенка от рождения": [ChildBusinessCard],
    "Личные качества": [QualitiesRevealedAgeOf20, ThirdTalentRevealedAge40],
    "Самореализация ребенка": [ChildOpportunity],
    "Точка душевного комфорта ребенка": [ChildPointOfComfort],
    "Задачи, которые тянутся из прошлых жизней": [MainTaskSoul, SoulPastExperiencesWithPeople, LessonsFromPastLife],
    "Предназначение ребенка": [ChildDestinyArcana1, ChildDestinyArcana2, ChildDestinyArcana3],
    "Детско-родительская карма": [WhatChildShouldTeachParents, WhatMistakesRelationshipParentsChildren, WhatShouldComeQualitiesChild],
}

def create_category(title, category_id):
    """Создает категорию, если она не существует."""
    category, created = ChildCategory.objects.get_or_create(id=category_id, defaults={"title": title})
    return category

def create_entries(model, category, title_prefix, description_prefix):
    """Создает 22 записи для заданной модели."""
    entries = [
        model(
            category=category,
            title=f"{title_prefix} {i}",
            description=escape(f"{description_prefix} {i}"),
            order_id=i,
        ) for i in range(1, 23)
    ]
    model.objects.bulk_create(entries)

class Command(BaseCommand):
    help = "Создает категории и заполняет таблицы данными"

    def handle(self, *args, **kwargs):
        # Создаем категории
        categories = {name: create_category(name, cat_id) for name, cat_id in CATEGORY_MAPPING.items()}
        
        # Заполняем таблицы
        for category_name, models in MODELS_MAPPING.items():
            category = categories[category_name]
            for model in models:
                create_entries(model, category, category_name, category_name)

        self.stdout.write(self.style.SUCCESS("База данных успешно заполнена! Категории и данные созданы."))

# python manage.py fill_child_data

