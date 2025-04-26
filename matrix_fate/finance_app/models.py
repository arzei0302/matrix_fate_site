from django.db import models
from ckeditor.fields import RichTextField
from matrix_fate.utils.mixins import OrderMarkerMixin


class FinanceCategory(models.Model):
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


# ТАЛАНТЫ - talents
class YourGreatestTalentBirth(OrderMarkerMixin):
    """Ваш главный талант от рождения (a)"""

    category = models.ForeignKey(
        FinanceCategory,
        on_delete=models.CASCADE,
        related_name="your_greatest_talent_birth",
    )
    title = models.CharField(
        max_length=255,
        verbose_name="Название",
        help_text="Ваш главный талант от рождения (a)",
    )
    description = RichTextField(
        verbose_name="Описание", help_text="Ваш главный талант от рождения (a)"
    )

    class Meta:
        verbose_name = "Ваш главный талант от рождения"
        verbose_name_plural = "Ваш главный талант от рождения"
        unique_together = ("category", "order_id")

    def __str__(self):
        return f"{self.category.title} - {self.title}"


class QualitiesRevealedAge20(OrderMarkerMixin):
    """Качества которые раскрываются к 20 годам (b)"""

    category = models.ForeignKey(
        FinanceCategory,
        on_delete=models.CASCADE,
        related_name="qualities_revealed_age_20",
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


class QualitiesDevelopAge40(OrderMarkerMixin):
    """Качества которые мы должны в себе наработать до 40 лет (c)"""

    category = models.ForeignKey(
        FinanceCategory,
        on_delete=models.CASCADE,
        related_name="qualities_develop_age_40",
    )
    title = models.CharField(
        max_length=255,
        verbose_name="Название",
        help_text="Качества которые мы должны в себе наработать до 40 лет (c)",
    )
    description = RichTextField(
        verbose_name="Описание",
        help_text="Качества которые мы должны в себе наработать до 40 лет (c)",
    )

    class Meta:
        verbose_name = "Качества которые мы должны в себе наработать до 40 лет"
        verbose_name_plural = "Качества которые мы должны в себе наработать до 40 лет"
        unique_together = ("category", "order_id")

    def __str__(self):
        return f"{self.category.title} - {self.title}"


# САМОРЕАЛИЗАЦИЯ - self_actualization
class YourOpportunity(OrderMarkerMixin):
    """Ваша возможность (a2)"""

    category = models.ForeignKey(
        FinanceCategory, on_delete=models.CASCADE, related_name="your_opportunity"
    )
    title = models.CharField(
        max_length=255, verbose_name="Название", help_text="Ваша возможность (a2)"
    )
    description = RichTextField(
        verbose_name="Описание", help_text="Ваша возможность (a2)"
    )

    class Meta:
        verbose_name = "Ваша возможность"
        verbose_name_plural = "Ваша возможность"
        unique_together = ("category", "order_id")

    def __str__(self):
        return f"{self.category.title} - {self.title}"


# ПРЕДНАЗНАЧЕНИЕ ДЛЯ СОЦИУМА - destination_society
class TaskPersonalArcana1(OrderMarkerMixin):
    """Задача для персонального аркана1 (t)"""

    category = models.ForeignKey(
        FinanceCategory, on_delete=models.CASCADE, related_name="task_personal_arcana_1"
    )
    title = models.CharField(
        max_length=255,
        verbose_name="Название",
        help_text="Задача для персонального аркана1 (t)",
    )
    description = RichTextField(
        verbose_name="Описание",
        help_text="Описание задачи для персонального аркана1 (t)",
    )

    class Meta:
        verbose_name = "Персональная задача 1"
        verbose_name_plural = "Персональные задачи 1"
        unique_together = ("category", "order_id")

    def __str__(self):
        return f"{self.category.title} - {self.title}"


class TaskPersonalArcana2(OrderMarkerMixin):
    """Задача для персонального аркана2 (u)"""

    category = models.ForeignKey(
        FinanceCategory, on_delete=models.CASCADE, related_name="task_personal_arcana_2"
    )
    title = models.CharField(
        max_length=255,
        verbose_name="Название",
        help_text="Задача для персонального аркана2 (u)",
    )
    description = RichTextField(
        verbose_name="Описание",
        help_text="Описание задачи для персонального аркана2 (u)",
    )

    class Meta:
        verbose_name = "Персональная задача 2"
        verbose_name_plural = "Персональные задачи 2"
        unique_together = ("category", "order_id")

    def __str__(self):
        return f"{self.category.title} - {self.title}"


class TaskPersonalArcana3(OrderMarkerMixin):
    """Задача для персонального аркана3 (v)"""

    category = models.ForeignKey(
        FinanceCategory, on_delete=models.CASCADE, related_name="task_personal_arcana_3"
    )
    title = models.CharField(
        max_length=255,
        verbose_name="Название",
        help_text="Задача для персонального аркана1 (v)",
    )
    description = RichTextField(
        verbose_name="Описание",
        help_text="Описание задачи для персонального аркана1 (v)",
    )

    class Meta:
        verbose_name = "Персональная задача 3"
        verbose_name_plural = "Персональные задачи 3"
        unique_together = ("category", "order_id")

    def __str__(self):
        return f"{self.category.title} - {self.title}"


# КАРМА И ЗАДАЧА 40 ЛЕТ - karma_and_task_40
class TheMainTask40Years(OrderMarkerMixin):
    """Главная задача 40 лет (c)"""

    category = models.ForeignKey(
        FinanceCategory, on_delete=models.CASCADE, related_name="the_main_task_40_years"
    )
    title = models.CharField(
        max_length=255, verbose_name="Название", help_text="Главная задача 40 лет (c)"
    )
    description = RichTextField(
        verbose_name="Описание", help_text="Главная задача 40 лет (c)"
    )

    class Meta:
        verbose_name = "Главная задача 40 лет"
        verbose_name_plural = "Главные задачи 40 лет"
        unique_together = ("category", "order_id")

    def __str__(self):
        return f"{self.category.title} - {self.title}"


class WhatBeforeYouTurn40Years(OrderMarkerMixin):
    """Что нужно сделать до 40 лет: (c1)"""

    category = models.ForeignKey(
        FinanceCategory,
        on_delete=models.CASCADE,
        related_name="what_before_you_turn_40_years",
    )
    title = models.CharField(
        max_length=255,
        verbose_name="Название",
        help_text="Что нужно сделать до 40 лет: (c1)",
    )
    description = RichTextField(
        verbose_name="Описание", help_text="Что нужно сделать до 40 лет: (c1)"
    )

    class Meta:
        verbose_name = "Что нужно сделать до 40 лет"
        verbose_name_plural = "Что нужно сделать до 40 лет"
        unique_together = ("category", "order_id")

    def __str__(self):
        return f"{self.category.title} - {self.title}"


class WhatAfterYouTurn40Years(OrderMarkerMixin):
    """Что нужно сделать после 40 лет: (c2)"""

    category = models.ForeignKey(
        FinanceCategory,
        on_delete=models.CASCADE,
        related_name="what_after_you_turn_40_years",
    )
    title = models.CharField(
        max_length=255,
        verbose_name="Название",
        help_text="Что нужно сделать после 40 лет: (c2)",
    )
    description = RichTextField(
        verbose_name="Описание", help_text="Что нужно сделать после 40 лет: (c2)"
    )

    class Meta:
        verbose_name = "Что нужно сделать после 40 лет"
        verbose_name_plural = "Что нужно сделать после 40 лет"
        unique_together = ("category", "order_id")

    def __str__(self):
        return f"{self.category.title} - {self.title}"


# ЧТО ДАЕТ ДЕНЬГИ - what_gives_you_money
class WhatGivesYouMoney(OrderMarkerMixin):
    """Что дает деньги (j)"""

    category = models.ForeignKey(
        FinanceCategory, on_delete=models.CASCADE, related_name="what_gives_you_money"
    )
    title = models.CharField(
        max_length=255, verbose_name="Название", help_text="Что дает деньги (j)"
    )
    description = RichTextField(
        verbose_name="Описание", help_text="Что дает деньги (j)"
    )

    class Meta:
        verbose_name = "Что дает деньги"
        verbose_name_plural = "Что дает деньги"
        unique_together = ("category", "order_id")

    def __str__(self):
        return f"{self.category.title} - {self.title}"


class WhatOpensYourMoneyChannel(OrderMarkerMixin):
    """Что открывает ваш денежный канал (l)"""

    category = models.ForeignKey(
        FinanceCategory,
        on_delete=models.CASCADE,
        related_name="what_opens_your_money_channel",
    )
    title = models.CharField(
        max_length=255,
        verbose_name="Название",
        help_text="Что открывает ваш денежный канал (l)",
    )
    description = RichTextField(
        verbose_name="Описание", help_text="Что открывает ваш денежный канал (l)"
    )

    class Meta:
        verbose_name = "Что открывает ваш денежный канал"
        verbose_name_plural = "Что открывает ваш денежный канал"
        unique_together = ("category", "order_id")

    def __str__(self):
        return f"{self.category.title} - {self.title}"


class AreasOfRealization(OrderMarkerMixin):
    """Сферы реализации (c2)"""

    category = models.ForeignKey(
        FinanceCategory, on_delete=models.CASCADE, related_name="areas_of_realization"
    )
    title = models.CharField(
        max_length=255, verbose_name="Название", help_text="Сферы реализации (c2)"
    )
    description = RichTextField(
        verbose_name="Описание", help_text="Сферы реализации (c2)"
    )

    class Meta:
        verbose_name = "Область реализации"
        verbose_name_plural = "Сферы реализации"
        unique_together = ("category", "order_id")

    def __str__(self):
        return f"{self.category.title} - {self.title}"


# ЧТО БЛОКИРУЕТ ДЕНЕЖНУЮ ЭНЕРГИЮ - what_blocks_money_energy
class TasksOpenMoneyChannel1(OrderMarkerMixin):
    """Какие нужно проработать задачи, чтобы раскрыть денежный канал: (l)"""

    category = models.ForeignKey(
        FinanceCategory,
        on_delete=models.CASCADE,
        related_name="tasks_open_money_channel1",
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
        verbose_name = "Задачаи открытия денежного канала1"
        verbose_name_plural = "Задачи открытия денежного канала1"
        unique_together = ("category", "order_id")

    def __str__(self):
        return f"{self.category.title} - {self.title}"


class TasksOpenMoneyChannel2(OrderMarkerMixin):
    """Какие нужно проработать задачи, чтобы раскрыть денежный канал: (c2)"""

    category = models.ForeignKey(
        FinanceCategory,
        on_delete=models.CASCADE,
        related_name="tasks_open_money_channel2",
    )
    title = models.CharField(
        max_length=255,
        verbose_name="Название",
        help_text="Какие нужно проработать задачи, чтобы раскрыть денежный канал: (c2)",
    )
    description = RichTextField(
        verbose_name="Описание",
        help_text="Какие нужно проработать задачи, чтобы раскрыть денежный канал: (c2)",
    )

    class Meta:
        verbose_name = "Задачаи открытия денежного канала2"
        verbose_name_plural = "Задачи открытия денежного канала2"
        unique_together = ("category", "order_id")

    def __str__(self):
        return f"{self.category.title} - {self.title}"


class WhatBlocksMoneyEnergy(OrderMarkerMixin):
    """Что блокирует денежную энергию: (j)"""

    category = models.ForeignKey(
        FinanceCategory,
        on_delete=models.CASCADE,
        related_name="what_blocks_money_energy",
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
        verbose_name = "Что блокирует денежную энергию"
        verbose_name_plural = "Что блокирует денежную энергию"
        unique_together = ("category", "order_id")

    def __str__(self):
        return f"{self.category.title} - {self.title}"


# ПРОГРАММЫ
class MatrixFinanceProgram(models.Model):
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
        verbose_name = "Программа Финансы"
        verbose_name_plural = "Программы Финансы"

    def __str__(self):
        return self.name
