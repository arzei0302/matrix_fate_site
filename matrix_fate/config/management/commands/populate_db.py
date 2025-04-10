from django.core.management.base import BaseCommand
from django.db import transaction
from matrix_fate_app.models import (
    Category,
    BirthTalent, YouthTalent, MatureTalent, 
    InnateTalent, YouthQualities, MatureQualities,
    MatureMission, PreMatureStepOne, PreMatureStepTwo, 
    SoulMission, PastLifeExperience, PastLifeLesson,
    PointMentalComfort, SelfRealization, FollowRecommendations, MustBeDone,
    ParentTeaching, FamilyRelationshipMistakes, PersonalGrowthGoal,
    SpiritualKarmaTask1, SpiritualKarmaTask2, SpiritualKarmaTask3,
    PartnerChallenges, IdealPartner, PartnerMeetingPlaces, RelationshipIssues,
    SuitableProfessions, MoneySources, FinancialGrowthTasks, WealthDevelopmentTasks, MoneyBlockages,
    PersonalArcan1, PersonalArcan2, PersonalArcan3,
    SocialArcan1, SocialArcan2, SocialArcan3,
    SpiritualPurpose, PlanetPurpose,
    MaleFatherLineageTasks, FemaleFatherLineageTasks,
    MaleMotherLineageTasks, FemaleMotherLineageTasks,
    Muladkhara_q1, Muladkhara_p1, Muladkhara_o1,
    Svadhisthana_o2, Svadhisthana_p2, Svadhisthana_q2,
    Manipura_o3, Manipura_p3, Manipura_q3,
    Anahata_o4, Anahata_p4, Anahata_q4,
    Vishuddha_o5, Vishuddha_p5, Vishuddha_q5,
    Ajna_o6, Ajna_p6, Ajna_q6,
    Sahasrara_o7, Sahasrara_p7, Sahasrara_q7,
    Total_o, Total_p, Total_q
)


class Command(BaseCommand):
    help = "Заполняет базу данных начальными данными (по 22 записи в каждую модель)"

    def handle(self, *args, **kwargs):
        with transaction.atomic():
            categories = self.get_existing_categories()
            self.create_records(categories)
            self.stdout.write(self.style.SUCCESS("База данных успешно заполнена!"))

    def get_existing_categories(self):
        """Получаем уже созданные вручную категории"""
        return {
            "Личные качества": Category.objects.get(title="Личные качества"),
            "Кем работать для души": Category.objects.get(title="Кем работать для души"),
            'Карма и задача 40 лет': Category.objects.get(title="Карма и задача 40 лет"),
            "Задачи которые тянутся из прошлых жизней": Category.objects.get(title="Задачи которые тянутся из прошлых жизней"),
            "Точка душевного комфорта": Category.objects.get(title="Точка душевного комфорта"),
            "Самореализация": Category.objects.get(title="Самореализация"),
            "Точка личной силы": Category.objects.get(title="Точка личной силы"),
            "Сила рода": Category.objects.get(title="Сила рода"),
            "Детско-родительская карма": Category.objects.get(title="Детско-родительская карма"),
            "Духовная карма": Category.objects.get(title="Духовная карма"),
            "Отношения в матрице": Category.objects.get(title="Отношения в матрице"),
            "Деньги в матрице": Category.objects.get(title="Деньги в матрице"),
            "Предназначение": Category.objects.get(title="Предназначение"),
            "Предрасположенность к заболеваниям": Category.objects.get(title="Предрасположенность к заболеваниям"),
            "Карта здоровья": Category.objects.get(title="Карта здоровья"),
        }


    def create_records(self, categories):
        """Создание 22 записей для каждой модели"""
        models_data = [
            {"model": BirthTalent, "category": categories["Личные качества"]},
            {"model": YouthTalent, "category": categories["Личные качества"]},
            {"model": MatureTalent, "category": categories["Личные качества"]},
            {"model": InnateTalent, "category": categories["Кем работать для души"]},
            {"model": YouthQualities, "category": categories["Кем работать для души"]},
            {"model": MatureQualities, "category": categories["Кем работать для души"]},
            {"model": MatureMission, "category": categories["Карма и задача 40 лет"]},
            {"model": PreMatureStepOne, "category": categories["Карма и задача 40 лет"]},
            {"model": PreMatureStepTwo, "category": categories["Карма и задача 40 лет"]},
            {"model": SoulMission, "category": categories["Задачи которые тянутся из прошлых жизней"]},
            {"model": PastLifeExperience, "category": categories["Задачи которые тянутся из прошлых жизней"]},
            {"model": PastLifeLesson, "category": categories["Задачи которые тянутся из прошлых жизней"],},
            {"model": PointMentalComfort, "category": categories["Точка душевного комфорта"]},
            {"model": SelfRealization, "category": categories["Самореализация"]},
            {"model": FollowRecommendations, "category": categories["Точка личной силы"]},
            {"model": MustBeDone, "category": categories["Сила рода"]},
            {"model": ParentTeaching, "category": categories["Детско-родительская карма"]},
            {"model": FamilyRelationshipMistakes, "category": categories["Детско-родительская карма"]},
            {"model": PersonalGrowthGoal, "category": categories["Детско-родительская карма"]},
            {"model": SpiritualKarmaTask1, "category": categories["Духовная карма"]},
            {"model": SpiritualKarmaTask2, "category": categories["Духовная карма"]},
            {"model": SpiritualKarmaTask3, "category": categories["Духовная карма"]},

            {"model": PartnerChallenges, "category": categories["Отношения в матрице"]},
            {"model": IdealPartner, "category": categories["Отношения в матрице"]},
            {"model": PartnerMeetingPlaces, "category": categories["Отношения в матрице"]},
            {"model": RelationshipIssues, "category": categories["Отношения в матрице"]},

            {"model": SuitableProfessions, "category": categories["Деньги в матрице"]},
            {"model": MoneySources, "category": categories["Деньги в матрице"]},
            {"model": FinancialGrowthTasks, "category": categories["Деньги в матрице"]},
            {"model": WealthDevelopmentTasks, "category": categories["Деньги в матрице"]},
            {"model": MoneyBlockages, "category": categories["Деньги в матрице"]},

            {"model": PersonalArcan1, "category": categories["Предназначение"]},
            {"model": PersonalArcan2, "category": categories["Предназначение"]},
            {"model": PersonalArcan3, "category": categories["Предназначение"]},
            {"model": SocialArcan1, "category": categories["Предназначение"]},
            {"model": SocialArcan2, "category": categories["Предназначение"]},
            {"model": SocialArcan3, "category": categories["Предназначение"]},
            {"model": SpiritualPurpose, "category": categories["Предназначение"]},
            {"model": PlanetPurpose, "category": categories["Предназначение"]},

            {"model": MaleFatherLineageTasks, "category": categories["Предрасположенность к заболеваниям"]},
            {"model": FemaleFatherLineageTasks, "category": categories["Предрасположенность к заболеваниям"]},
            {"model": MaleMotherLineageTasks, "category": categories["Предрасположенность к заболеваниям"]},
            {"model": FemaleMotherLineageTasks, "category": categories["Предрасположенность к заболеваниям"]},

            {"model": Muladkhara_o1, "category": categories["Карта здоровья"]},
            {"model": Muladkhara_p1, "category": categories["Карта здоровья"]},
            {"model": Muladkhara_q1, "category": categories["Карта здоровья"]},

            {"model": Svadhisthana_o2, "category": categories["Карта здоровья"]},
            {"model": Svadhisthana_p2, "category": categories["Карта здоровья"]},
            {"model": Svadhisthana_q2, "category": categories["Карта здоровья"]},

            {"model": Manipura_o3, "category": categories["Карта здоровья"]},
            {"model": Manipura_p3, "category": categories["Карта здоровья"]},
            {"model": Manipura_q3, "category": categories["Карта здоровья"]},

            {"model": Anahata_o4, "category": categories["Карта здоровья"]},
            {"model": Anahata_p4, "category": categories["Карта здоровья"]},
            {"model": Anahata_q4, "category": categories["Карта здоровья"]},

            {"model": Vishuddha_o5, "category": categories["Карта здоровья"]},
            {"model": Vishuddha_p5, "category": categories["Карта здоровья"]},
            {"model": Vishuddha_q5, "category": categories["Карта здоровья"]},

            {"model": Ajna_o6, "category": categories["Карта здоровья"]},
            {"model": Ajna_p6, "category": categories["Карта здоровья"]},
            {"model": Ajna_q6, "category": categories["Карта здоровья"]},

            {"model": Sahasrara_o7, "category": categories["Карта здоровья"]},
            {"model": Sahasrara_p7, "category": categories["Карта здоровья"]},
            {"model": Sahasrara_q7, "category": categories["Карта здоровья"]},

            {"model": Total_o, "category": categories["Карта здоровья"]},
            {"model": Total_p, "category": categories["Карта здоровья"]},
            {"model": Total_q, "category": categories["Карта здоровья"]},
        ]

        for model_data in models_data:
            model = model_data["model"]
            category = model_data["category"]

            for i in range(1, 23):  # 22 записи (ровно от 1 до 22)
                order = i  # Теперь order = 1, 2, ... 22
                title = f"{model.__name__} {i}"  # Пронумерованный заголовок
                description = f"Описание для {model.__name__} номер {i}"  # Пронумерованное описание

                obj, created = model.objects.get_or_create(
                    title=title,
                    category=category,
                    defaults={"order": order, "description": description}
                )

                if created:
                    self.stdout.write(self.style.SUCCESS(f'Добавлена запись: {title} (order={order})'))
                else:
                    self.stdout.write(self.style.WARNING(f'Запись уже существует: {title}'))
