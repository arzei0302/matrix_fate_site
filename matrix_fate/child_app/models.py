from django.db import models
from ckeditor.fields import RichTextField
from utils.mixins import OrderMarkerMixin


class ChildCategory(models.Model):
    """Категория Детской матрицы"""

    title = models.CharField(
        max_length=255,
        verbose_name="Название категории",
        help_text="Название категории",
    )
    description = RichTextField(
        verbose_name="Описание категории", help_text="Описание категории"
    )
    is_paid = models.BooleanField(default=False, verbose_name="Платная категория")

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.title


# Главный талант ребенка от рождения - child_greatest_talent#
class ChildBusinessCard(OrderMarkerMixin):
    """Визитная карточка ребенка (a)"""

    category = models.ForeignKey(
        ChildCategory, on_delete=models.CASCADE, related_name="child_business_card"
    )
    title = models.CharField(
        max_length=255,
        verbose_name="Название",
        help_text="Визитная карточка ребенка (a)",
    )
    description = RichTextField(
        verbose_name="Описание", help_text="Визитная карточка ребенка (a)"
    )

    class Meta:
        verbose_name = "Визитная карточка ребенка (a)"
        verbose_name_plural = "Визитная карточка ребенка (a)"
        unique_together = ("category", "order_id")

    def __str__(self):
        return f"{self.category.title} - {self.title}"


# Личные качества - child_personal_qualities#
class QualitiesRevealedAgeOf20(OrderMarkerMixin):
    """Качества которые раскрываются к 20 годам (b)"""

    category = models.ForeignKey(
        ChildCategory,
        on_delete=models.CASCADE,
        related_name="qualities_revealed_age_of_20",
    )
    title = models.CharField(
        max_length=255,
        verbose_name="Название",
        help_text="Качества которые раскрываются к 20 годам (b)",
    )
    description = RichTextField(
        verbose_name="Описание",
        help_text="Качества которые раскрываются к 20 годам (b)",
    )

    class Meta:
        verbose_name = "Качества которые раскрываются к 20 годам"
        verbose_name_plural = "Качества которые раскрываются к 20 годам"
        unique_together = ("category", "order_id")

    def __str__(self):
        return f"{self.category.title} - {self.title}"


class ThirdTalentRevealedAge40(OrderMarkerMixin):
    """Третий талант раскрывается к 40 годам (c)"""

    category = models.ForeignKey(
        ChildCategory,
        on_delete=models.CASCADE,
        related_name="third_talent_revealed_age_40",
    )
    title = models.CharField(
        max_length=255,
        verbose_name="Название",
        help_text="Третий талант раскрывается к 40 годам (c)",
    )
    description = RichTextField(
        verbose_name="Описание", help_text="Третий талант раскрывается к 40 годам (c)"
    )

    class Meta:
        verbose_name = "Третий талант раскрывается к 40 годам"
        verbose_name_plural = "Третий талант раскрывается к 40 годам"
        unique_together = ("category", "order_id")

    def __str__(self):
        return f"{self.category.title} - {self.title}"


# Самореализация ребенка - child_self_realization#
class ChildOpportunity(OrderMarkerMixin):
    """Возможность ребенка: (a2)"""

    category = models.ForeignKey(
        ChildCategory, on_delete=models.CASCADE, related_name="child_opportunity"
    )
    title = models.CharField(
        max_length=255, verbose_name="Название", help_text="Возможность ребенка: (a2)"
    )
    description = RichTextField(
        verbose_name="Описание", help_text="Возможность ребенка: (a2)"
    )

    class Meta:
        verbose_name = "Возможность ребенка"
        verbose_name_plural = "Возможность ребенка"
        unique_together = ("category", "order_id")

    def __str__(self):
        return f"{self.category.title} - {self.title}"


# Точка душевного комфорта ребенка - child_point_of_comfort
class ChildPointOfComfort(OrderMarkerMixin):
    """Аркан точки душевного комфорта ребенка: (e)"""

    category = models.ForeignKey(
        ChildCategory, on_delete=models.CASCADE, related_name="child_point_of_comfort"
    )
    title = models.CharField(
        max_length=255,
        verbose_name="Название",
        help_text="Аркан точки душевного комфорта ребенка: (e)",
    )
    description = RichTextField(
        verbose_name="Описание", help_text="Аркан точки душевного комфорта ребенка: (e)"
    )

    class Meta:
        verbose_name = "Аркан точки душевного комфорта ребенка"
        verbose_name_plural = "Аркан точки душевного комфорта ребенка"
        unique_together = ("category", "order_id")

    def __str__(self):
        return f"{self.category.title} - {self.title}"


# Задачи, которые тянутся из прошлых жизней - tasks_from_past_lives
class MainTaskSoul(OrderMarkerMixin):
    """Главная задача Души (d)"""

    category = models.ForeignKey(
        ChildCategory, on_delete=models.CASCADE, related_name="main_task_soul"
    )
    title = models.CharField(
        max_length=255, verbose_name="Название", help_text="Главная задача Души (d)"
    )
    description = RichTextField(
        verbose_name="Описание", help_text="Главная задача Души (d)"
    )

    class Meta:
        verbose_name = "Главная задача Души"
        verbose_name_plural = "Главная задача Души"
        unique_together = ("category", "order_id")

    def __str__(self):
        return f"{self.category.title} - {self.title}"


class SoulPastExperiencesWithPeople(OrderMarkerMixin):
    """Опыт души в прошлом с людьми (d2)"""

    category = models.ForeignKey(
        ChildCategory,
        on_delete=models.CASCADE,
        related_name="soul_past_experiences_with_people",
    )
    title = models.CharField(
        max_length=255,
        verbose_name="Название",
        help_text="Опыт души в прошлом с людьми (d2)",
    )
    description = RichTextField(
        verbose_name="Описание", help_text="Опыт души в прошлом с людьми (d2)"
    )

    class Meta:
        verbose_name = "Опыт души в прошлом с людьми"
        verbose_name_plural = "Опыт души в прошлом с людьми"
        unique_together = ("category", "order_id")

    def __str__(self):
        return f"{self.category.title} - {self.title}"


class LessonsFromPastLife(OrderMarkerMixin):
    """Урок из прошлой жизни (d1)"""

    category = models.ForeignKey(
        ChildCategory, on_delete=models.CASCADE, related_name="lessons_from_past_life"
    )
    title = models.CharField(
        max_length=255, verbose_name="Название", help_text="Урок из прошлой жизни (d1)"
    )
    description = RichTextField(
        verbose_name="Описание", help_text="Урок из прошлой жизни (d1)"
    )

    class Meta:
        verbose_name = "Урок из прошлой жизни"
        verbose_name_plural = "Урок из прошлой жизни"
        unique_together = ("category", "order_id")

    def __str__(self):
        return f"{self.category.title} - {self.title}"


# Предназначение ребенка - child_destiny
class ChildDestinyArcana1(OrderMarkerMixin):
    """Предназначение ребенка (r)"""

    category = models.ForeignKey(
        ChildCategory, on_delete=models.CASCADE, related_name="child_destiny_arcana1"
    )
    title = models.CharField(
        max_length=255, verbose_name="Название", help_text="Предназначение ребенка (r)"
    )
    description = RichTextField(
        verbose_name="Описание", help_text="Предназначение ребенка (r)"
    )

    class Meta:
        verbose_name = "Предназначение ребенка"
        verbose_name_plural = "Предназначение ребенка"
        unique_together = ("category", "order_id")

    def __str__(self):
        return f"{self.category.title} - {self.title}"


class ChildDestinyArcana2(OrderMarkerMixin):
    """Предназначение ребенка (s)"""

    category = models.ForeignKey(
        ChildCategory, on_delete=models.CASCADE, related_name="child_destiny_arcana2"
    )
    title = models.CharField(
        max_length=255, verbose_name="Название", help_text="Предназначение ребенка (s)"
    )
    description = RichTextField(
        verbose_name="Описание", help_text="Предназначение ребенка (s)"
    )

    class Meta:
        verbose_name = "Предназначение ребенка"
        verbose_name_plural = "Предназначение ребенка"
        unique_together = ("category", "order_id")

    def __str__(self):
        return f"{self.category.title} - {self.title}"


class ChildDestinyArcana3(OrderMarkerMixin):
    """Предназначение ребенка (y)"""

    category = models.ForeignKey(
        ChildCategory, on_delete=models.CASCADE, related_name="child_destiny_arcana3"
    )
    title = models.CharField(
        max_length=255, verbose_name="Название", help_text="Предназначение ребенка (y)"
    )
    description = RichTextField(
        verbose_name="Описание", help_text="Предназначение ребенка (y)"
    )

    class Meta:
        verbose_name = "Предназначение ребенка"
        verbose_name_plural = "Предназначение ребенка"
        unique_together = ("category", "order_id")

    def __str__(self):
        return f"{self.category.title} - {self.title}"


# Детско-родительская карма - child_parent_karma
class WhatChildShouldTeachParents(OrderMarkerMixin):
    """Чему ребенок должен научить своих родителей: (a)"""

    category = models.ForeignKey(
        ChildCategory,
        on_delete=models.CASCADE,
        related_name="what_child_should_teach_parents",
    )
    title = models.CharField(
        max_length=255,
        verbose_name="Название",
        help_text="Чему ребенок должен научить своих родителей: (a)",
    )
    description = RichTextField(
        verbose_name="Описание",
        help_text="Чему ребенок должен научить своих родителей: (a)",
    )

    class Meta:
        verbose_name = "Чему ребенок должен научить своих родителей"
        verbose_name_plural = "Чему ребенок должен научить своих родителей"
        unique_together = ("category", "order_id")

    def __str__(self):
        return f"{self.category.title} - {self.title}"


class WhatMistakesRelationshipParentsChildren(OrderMarkerMixin):
    """Какие могут быть ошибки во взаимоотношениях с родителями и своими детьми:(a2)"""

    category = models.ForeignKey(
        ChildCategory,
        on_delete=models.CASCADE,
        related_name="what_mistakes_relationship_parents_children",
    )
    title = models.CharField(
        max_length=255,
        verbose_name="Название",
        help_text="Какие могут быть ошибки во взаимоотношениях с родителями и своими детьми:(a2)",
    )
    description = RichTextField(
        verbose_name="Описание",
        help_text="Какие могут быть ошибки во взаимоотношениях с родителями и своими детьми:(a2)",
    )

    class Meta:
        verbose_name = (
            "Какие могут быть ошибки во взаимоотношениях с родителями и своими детьми"
        )
        verbose_name_plural = (
            "Какие могут быть ошибки во взаимоотношениях с родителями и своими детьми"
        )
        unique_together = ("category", "order_id")

    def __str__(self):
        return f"{self.category.title} - {self.title}"


class WhatShouldComeQualitiesChild(OrderMarkerMixin):
    """К чему должны прийти, какие качества необходимо наработать ребенку: (a1)"""

    category = models.ForeignKey(
        ChildCategory,
        on_delete=models.CASCADE,
        related_name="what_should_come_qualities_child",
    )
    title = models.CharField(
        max_length=255,
        verbose_name="Название",
        help_text="К чему должны прийти, какие качества необходимо наработать ребенку: (a1)",
    )
    description = RichTextField(
        verbose_name="Описание",
        help_text="К чему должны прийти, какие качества необходимо наработать ребенку: (a1)",
    )

    class Meta:
        verbose_name = (
            "К чему должны прийти, какие качества необходимо наработать ребенку"
        )
        verbose_name_plural = (
            "К чему должны прийти, какие качества необходимо наработать ребенку"
        )
        unique_together = ("category", "order_id")

    def __str__(self):
        return f"{self.category.title} - {self.title}"


# ПРОГРАММЫ
class MatrixChildProgram(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название программы")

    marker_1_name = models.CharField(
        max_length=3, verbose_name="Маркер 1", help_text="Пример: a, a1, a2"
    )
    marker_1_value = models.IntegerField(
        verbose_name="Значение маркера 1",
        help_text="Значение от 1 до 22",
        choices=[(i, i) for i in range(1, 23)],
    )

    marker_2_name = models.CharField(
        max_length=3, verbose_name="Маркер 2", help_text="Пример: b, b1, b2"
    )
    marker_2_value = models.IntegerField(
        verbose_name="Значение маркера 2",
        help_text="Значение от 1 до 22",
        choices=[(i, i) for i in range(1, 23)],
    )

    marker_3_name = models.CharField(
        max_length=3, verbose_name="Маркер 3", help_text="Пример: m, n, c2"
    )
    marker_3_value = models.IntegerField(
        verbose_name="Значение маркера 3",
        help_text="Значение от 1 до 22",
        choices=[(i, i) for i in range(1, 23)],
    )

    description = RichTextField(blank=True, verbose_name="Описание программы")

    class Meta:
        verbose_name = "Программа Детская"
        verbose_name_plural = "Программы Детская"

    def __str__(self):
        return self.name
