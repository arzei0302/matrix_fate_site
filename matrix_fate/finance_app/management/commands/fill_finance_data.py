from django.core.management.base import BaseCommand
from django.utils.html import escape
from finance_app.models import (
    FinanceCategory, YourGreatestTalentBirth, QualitiesRevealedAge20, QualitiesDevelopAge40,
    YourOpportunity, TaskPersonalArcana1, TaskPersonalArcana2, TaskPersonalArcana3,
    WhatGivesYouMoney, WhatOpensYourMoneyChannel, AreasOfRealization,
    TasksOpenMoneyChannel1, TasksOpenMoneyChannel2, WhatBlocksMoneyEnergy
)

CATEGORY_MAPPING = {
    "Таланты": 1,
    "Самореализация": 2,
    "Предназначение для социума": 3,
    "Карма и задача 40 лет": 4,
    "Что блокирует денежную энергию": 5,
}

def create_entries(model, category_id, title_prefix, description_prefix):
    category = FinanceCategory.objects.get(id=category_id)
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
        create_entries(YourGreatestTalentBirth, CATEGORY_MAPPING["Таланты"], "Талант", "Описание таланта")
        create_entries(QualitiesRevealedAge20, CATEGORY_MAPPING["Таланты"], "Качество к 20 годам", "Описание качества к 20 годам")
        create_entries(QualitiesDevelopAge40, CATEGORY_MAPPING["Таланты"], "Качество к 40 годам", "Описание качества к 40 годам")
        create_entries(YourOpportunity, CATEGORY_MAPPING["Самореализация"], "Возможность", "Описание возможности")
        create_entries(TaskPersonalArcana1, CATEGORY_MAPPING["Предназначение для социума"], "Задача 1", "Описание задачи 1")
        create_entries(TaskPersonalArcana2, CATEGORY_MAPPING["Предназначение для социума"], "Задача 2", "Описание задачи 2")
        create_entries(TaskPersonalArcana3, CATEGORY_MAPPING["Предназначение для социума"], "Задача 3", "Описание задачи 3")
        create_entries(WhatGivesYouMoney, CATEGORY_MAPPING["Карма и задача 40 лет"], "Фактор денег", "Описание фактора денег")
        create_entries(WhatOpensYourMoneyChannel, CATEGORY_MAPPING["Карма и задача 40 лет"], "Открытие денежного канала", "Описание открытия денежного канала")
        create_entries(AreasOfRealization, CATEGORY_MAPPING["Карма и задача 40 лет"], "Сфера реализации", "Описание сферы реализации")
        create_entries(TasksOpenMoneyChannel1, CATEGORY_MAPPING["Что блокирует денежную энергию"], "Задача 1 для денег", "Описание задачи 1 для денег")
        create_entries(TasksOpenMoneyChannel2, CATEGORY_MAPPING["Что блокирует денежную энергию"], "Задача 2 для денег", "Описание задачи 2 для денег")
        create_entries(WhatBlocksMoneyEnergy, CATEGORY_MAPPING["Что блокирует денежную энергию"], "Блокировка энергии", "Описание блокировки энергии")
        
        self.stdout.write(self.style.SUCCESS("База данных успешно заполнена 22 записями в каждую таблицу!"))


# python manage.py fill_finance_data