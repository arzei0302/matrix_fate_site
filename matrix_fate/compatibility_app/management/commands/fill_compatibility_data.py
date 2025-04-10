from django.core.management.base import BaseCommand
from django.utils.html import escape
from compatibility_app.models import (
    CompatibilityCategory,
    WhyDidYouMeet,
    TasksForCoupleArcana1, TasksForCoupleArcana2, TasksForCoupleArcana3,
    CoupleResourcesArcana1, CoupleResourcesArcana2,
    WhatFillsTheVapor,
    CouplesTaskForSociety,
    WhatGivesTribute, WhatTasksUnlockMoneyChannels, WhatBlocksMonetaryEnergy,
    CoupleRelations1, CoupleRelations2, WhatRelationshipProblemsCanArise,
)

CATEGORY_MAPPING = {
    "Для чего вы встретились": 1,
    "Задачи для пары": 2,
    "Ресурсы пары": 3,
    "От чего наполняется пара": 4,
    "Задача пары для социума": 5,
    "Деньги в паре": 6,
    "Отношения в паре": 7,
}

def create_entries(model, category_id, title_prefix, description_prefix):
    category = CompatibilityCategory.objects.get(id=category_id)
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
    help = "Заполняет таблицы данными"

    def handle(self, *args, **kwargs):
        create_entries(WhyDidYouMeet, CATEGORY_MAPPING["Для чего вы встретились"], "Для чего вы встретились", "Для чего вы встретились")

        create_entries(TasksForCoupleArcana1, CATEGORY_MAPPING["Задачи для пары"], "Задачи для пары1", "Задачи для пары1")
        create_entries(TasksForCoupleArcana2, CATEGORY_MAPPING["Задачи для пары"], "Задачи для пары2", "Задачи для пары2")
        create_entries(TasksForCoupleArcana3, CATEGORY_MAPPING["Задачи для пары"], "Задачи для пары3", "Задачи для пары3")
        
        create_entries(CoupleResourcesArcana1, CATEGORY_MAPPING["Ресурсы пары"], "Ресурсы пары 1", "Ресурсы пары 1")
        create_entries(CoupleResourcesArcana2, CATEGORY_MAPPING["Ресурсы пары"], "Ресурсы пары 2", "Ресурсы пары 2")

        create_entries(WhatFillsTheVapor, CATEGORY_MAPPING["От чего наполняется пара"], "От чего наполняется пара", "От чего наполняется пара")

        create_entries(CouplesTaskForSociety, CATEGORY_MAPPING["Задача пары для социума"], "Задача пары для социума", "Задача пары для социума")

        create_entries(WhatGivesTribute, CATEGORY_MAPPING["Деньги в паре"], "Деньги в паре", "Деньги в паре")
        create_entries(WhatTasksUnlockMoneyChannels, CATEGORY_MAPPING["Деньги в паре"], "Деньги в паре", "Деньги в паре")
        create_entries(WhatBlocksMonetaryEnergy, CATEGORY_MAPPING["Деньги в паре"], "Деньги в паре", "Деньги в паре")

        create_entries(CoupleRelations1, CATEGORY_MAPPING["Отношения в паре"], "Отношения в паре", "Отношения в паре")
        create_entries(CoupleRelations2, CATEGORY_MAPPING["Отношения в паре"], "Отношения в паре", "Отношения в паре")
        create_entries(WhatRelationshipProblemsCanArise, CATEGORY_MAPPING["Отношения в паре"], "Отношения в паре", "Отношения в паре")
        
        self.stdout.write(self.style.SUCCESS("База данных успешно заполнена 22 записями в каждую таблицу!"))


# python manage.py fill_compatibility_data
