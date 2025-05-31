from django.db import models
from ckeditor.fields import RichTextField
from matrix_fate.utils.mixins import OrderMarkerMixin


class CompatibilityCategory(models.Model):
    """Категория Финансы (например, Сферы реализации)"""

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


# Для чего вы встретились - why_did_you_meet
class WhyDidYouMeet(OrderMarkerMixin):
    """Для чего вы встретились (a)"""

    category = models.ForeignKey(
        CompatibilityCategory, on_delete=models.CASCADE, related_name="why_did_you_meet"
    )
    title = models.CharField(
        max_length=255, verbose_name="Название", help_text="Для чего вы встретились (a)"
    )
    description = RichTextField(
        verbose_name="Описание", help_text="Для чего вы встретились (a)"
    )
    

    class Meta:
        verbose_name = "Для чего вы встретились"
        verbose_name_plural = "Для чего вы встретились"
        unique_together = ("category", "order_id")

    def __str__(self):
        return f"{self.category.title} - {self.title}"


# Задачи для пары - tasks_for_couple
class TasksForCoupleArcana1(OrderMarkerMixin):
    """Задачи для пары (w)"""

    category = models.ForeignKey(
        CompatibilityCategory,
        on_delete=models.CASCADE,
        related_name="tasks_for_couple_w",
    )
    title = models.CharField(
        max_length=255, verbose_name="Название", help_text="Задачи для пары (w)"
    )
    description = RichTextField(
        verbose_name="Описание", help_text="Задачи для пары (w)"
    )
    

    class Meta:
        verbose_name = "Задачи для пары (w)"
        verbose_name_plural = "Задачи для пары (w)"
        unique_together = ("category", "order_id")

    def __str__(self):
        return f"{self.category.title} - {self.title}"


class TasksForCoupleArcana2(OrderMarkerMixin):
    """Задачи для пары (d)"""

    category = models.ForeignKey(
        CompatibilityCategory,
        on_delete=models.CASCADE,
        related_name="tasks_for_couple_d",
    )
    title = models.CharField(
        max_length=255, verbose_name="Название", help_text="Задачи для пары (d)"
    )
    description = RichTextField(
        verbose_name="Описание", help_text="Задачи для пары (d)"
    )
    

    class Meta:
        verbose_name = "Задачи для пары (d)"
        verbose_name_plural = "Задачи для пары (d)"
        unique_together = ("category", "order_id")

    def __str__(self):
        return f"{self.category.title} - {self.title}"


class TasksForCoupleArcana3(OrderMarkerMixin):
    """Задачи для пары (y)"""

    category = models.ForeignKey(
        CompatibilityCategory,
        on_delete=models.CASCADE,
        related_name="tasks_for_couple_y",
    )
    title = models.CharField(
        max_length=255, verbose_name="Название", help_text="Задачи для пары (y)"
    )
    description = RichTextField(
        verbose_name="Описание", help_text="Задачи для пары (y)"
    )
    

    class Meta:
        verbose_name = "Задачи для пары (y)"
        verbose_name_plural = "Задачи для пары (y)"
        unique_together = ("category", "order_id")

    def __str__(self):
        return f"{self.category.title} - {self.title}"


# Ресурсы пары - couple_resources
class CoupleResourcesArcana1(OrderMarkerMixin):
    """Ресурсы пары (b)"""

    category = models.ForeignKey(
        CompatibilityCategory,
        on_delete=models.CASCADE,
        related_name="couple_resources_b",
    )
    title = models.CharField(
        max_length=255, verbose_name="Название", help_text="Ресурсы пары (b)"
    )
    description = RichTextField(verbose_name="Описание", help_text="Ресурсы пары (b)")
    

    class Meta:
        verbose_name = "Ресурсы пары (b)"
        verbose_name_plural = "Ресурсы пары (b)"
        unique_together = ("category", "order_id")

    def __str__(self):
        return f"{self.category.title} - {self.title}"


class CoupleResourcesArcana2(OrderMarkerMixin):
    """Ресурсы пары (c)"""

    category = models.ForeignKey(
        CompatibilityCategory,
        on_delete=models.CASCADE,
        related_name="couple_resources_c",
    )
    title = models.CharField(
        max_length=255, verbose_name="Название", help_text="Ресурсы пары (c)"
    )
    description = RichTextField(verbose_name="Описание", help_text="Ресурсы пары (c)")
    

    class Meta:
        verbose_name = "Ресурсы пары (c)"
        verbose_name_plural = "Ресурсы пары (c)"
        unique_together = ("category", "order_id")

    def __str__(self):
        return f"{self.category.title} - {self.title}"


# От чего наполняется пара - what_fills_the_vapor
class WhatFillsTheVapor(OrderMarkerMixin):
    """От чего наполняется пара (e)"""

    category = models.ForeignKey(
        CompatibilityCategory,
        on_delete=models.CASCADE,
        related_name="what_fills_the_vapor_e",
    )
    title = models.CharField(
        max_length=255,
        verbose_name="Название",
        help_text="От чего наполняется пара (e)",
    )
    description = RichTextField(
        verbose_name="Описание", help_text="От чего наполняется пара (e)"
    )
    

    class Meta:
        verbose_name = "От чего наполняется пара (e)"
        verbose_name_plural = "От чего наполняется пара (e)"
        unique_together = ("category", "order_id")

    def __str__(self):
        return f"{self.category.title} - {self.title}"


# Задача пары для социума - couples_task_for_society
class CouplesTaskForSociety(OrderMarkerMixin):
    """Задача пары для социума (v)"""

    category = models.ForeignKey(
        CompatibilityCategory,
        on_delete=models.CASCADE,
        related_name="couples_task_for_society_v",
    )
    title = models.CharField(
        max_length=255, verbose_name="Название", help_text="Задача пары для социума (v)"
    )
    description = RichTextField(
        verbose_name="Описание", help_text="Задача пары для социума (v)"
    )
    

    class Meta:
        verbose_name = "Задача пары для социума (v)"
        verbose_name_plural = "Задача пары для социума (v)"
        unique_together = ("category", "order_id")

    def __str__(self):
        return f"{self.category.title} - {self.title}"


# Деньги в паре - couple_money
class WhatGivesTribute(OrderMarkerMixin):
    """Что дает деньги (c2)"""

    category = models.ForeignKey(
        CompatibilityCategory,
        on_delete=models.CASCADE,
        related_name="what_gives_tribute_c2",
    )
    title = models.CharField(
        max_length=255, verbose_name="Название", help_text="Что дает деньги (c2)"
    )
    description = RichTextField(
        verbose_name="Описание", help_text="Что дает деньги (c2)"
    )
    

    class Meta:
        verbose_name = "Что дает деньги (c2)"
        verbose_name_plural = "Что дает деньги (c2)"
        unique_together = ("category", "order_id")

    def __str__(self):
        return f"{self.category.title} - {self.title}"


class WhatTasksUnlockMoneyChannels(OrderMarkerMixin):
    """Какие нужно проработать задачи, чтобы раскрыть денежный канал: (l)"""

    category = models.ForeignKey(
        CompatibilityCategory,
        on_delete=models.CASCADE,
        related_name="what_tasks_unlock_money_channels_l",
    )
    title = models.CharField(
        max_length=255,
        verbose_name="Название",
        help_text="Какие нужно проработать задачи, чтобы раскрыть денежный канал: (l)",
    )
    description = RichTextField(
        verbose_name="Описание",
        help_text="Какие нужно проработать задачи, чтобы раскрыть денежный канал: (l)",
    )
    

    class Meta:
        verbose_name = (
            "Какие нужно проработать задачи, чтобы раскрыть денежный канал: (l)"
        )
        verbose_name_plural = (
            "Какие нужно проработать задачи, чтобы раскрыть денежный канал: (l)"
        )
        unique_together = ("category", "order_id")

    def __str__(self):
        return f"{self.category.title} - {self.title}"


class WhatBlocksMonetaryEnergy(OrderMarkerMixin):
    """Что блокирует денежную энергию: (j)"""

    category = models.ForeignKey(
        CompatibilityCategory,
        on_delete=models.CASCADE,
        related_name="what_blocks_monetary_energy_j",
    )
    title = models.CharField(
        max_length=255,
        verbose_name="Название",
        help_text="Что блокирует денежную энергию: (j)",
    )
    description = RichTextField(
        verbose_name="Описание", help_text="Что блокирует денежную энергию: (j)"
    )
    

    class Meta:
        verbose_name = "Что блокирует денежную энергию: (j)"
        verbose_name_plural = "Что блокирует денежную энергию: (j)"
        unique_together = ("category", "order_id")

    def __str__(self):
        return f"{self.category.title} - {self.title}"


# Отношения в паре - couple_relations
class CoupleRelations1(OrderMarkerMixin):
    """Отношения в паре (d2)"""

    category = models.ForeignKey(
        CompatibilityCategory,
        on_delete=models.CASCADE,
        related_name="couple_relations_d2",
    )
    title = models.CharField(
        max_length=255, verbose_name="Название", help_text="Отношения в паре (d2)"
    )
    description = RichTextField(
        verbose_name="Описание", help_text="Отношения в паре (d2)"
    )
    

    class Meta:
        verbose_name = "Отношения в паре (d2)"
        verbose_name_plural = "Отношения в паре (d2)"
        unique_together = ("category", "order_id")

    def __str__(self):
        return f"{self.category.title} - {self.title}"


class CoupleRelations2(OrderMarkerMixin):
    """Отношения в паре (k)"""

    category = models.ForeignKey(
        CompatibilityCategory,
        on_delete=models.CASCADE,
        related_name="couple_relations_k",
    )
    title = models.CharField(
        max_length=255, verbose_name="Название", help_text="Отношения в паре (k)"
    )
    description = RichTextField(
        verbose_name="Описание", help_text="Отношения в паре (k)"
    )
    

    class Meta:
        verbose_name = "Отношения в паре (k)"
        verbose_name_plural = "Отношения в паре (k)"
        unique_together = ("category", "order_id")

    def __str__(self):
        return f"{self.category.title} - {self.title}"


class WhatRelationshipProblemsCanArise(OrderMarkerMixin):
    """Какие могут возникнуть проблемы в отношениях: (j)"""

    category = models.ForeignKey(
        CompatibilityCategory,
        on_delete=models.CASCADE,
        related_name="what_relationship_problems_can_arise_j",
    )
    title = models.CharField(
        max_length=255,
        verbose_name="Название",
        help_text="Какие могут возникнуть проблемы в отношениях: (j)",
    )
    description = RichTextField(
        verbose_name="Описание",
        help_text="Какие могут возникнуть проблемы в отношениях: (j)",
    )
    

    class Meta:
        verbose_name = "Какие могут возникнуть проблемы в отношениях: (j)"
        verbose_name_plural = "Какие могут возникнуть проблемы в отношениях: (j)"
        unique_together = ("category", "order_id")

    def __str__(self):
        return f"{self.category.title} - {self.title}"
    

# ПРОГРАММЫ
class MatrixCompatibilityProgram(models.Model):
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
    is_paid = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Программа Совместимости"
        verbose_name_plural = "Программы Совместимости"

    def __str__(self):
        return self.name
