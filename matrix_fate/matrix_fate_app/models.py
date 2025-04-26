from django.db import models
from ckeditor.fields import RichTextField
from matrix_fate.utils.mixins import OrderMarkerMixin

class Category(models.Model):
    """Категория Матрицы Судьбы"""

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


# ЛИЧНЫЕ КАЧЕСТВА - personal_qualities
class BirthTalent(OrderMarkerMixin):
    """Главный талант данный при рождении (a)"""

    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="birth_talents"
    )
    title = models.CharField(
        max_length=255,
        verbose_name="Название",
        help_text="Главный талант данный при рождении (a)",
    )
    description = RichTextField(
        verbose_name="Описание", help_text="Главный талант данный при рождении (a)"
    )
    
    

    class Meta:
        verbose_name = "Главный талант данный при рождении"
        verbose_name_plural = "Главный талант данный при рождении"
        unique_together = ("category", "order_id")

    def __str__(self):
        return f"{self.category.title} - {self.title}"


class YouthTalent(OrderMarkerMixin):
    """Второй талант раскрывается к 20 годам (b)"""

    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="youth_talents"
    )
    title = models.CharField(
        max_length=255,
        verbose_name="Название",
        help_text="Второй талант раскрывается к 20 годам (b)",
    )
    description = RichTextField(
        verbose_name="Описание", help_text="Второй талант раскрывается к 20 годам (b)"
    )
    
    class Meta:
        unique_together = ("category", "order_id")
        verbose_name = "Второй талант раскрывается к 20 годам"
        verbose_name_plural = "Второй талант раскрывается к 20 годам"

    def __str__(self):
        return f"{self.category.title} - {self.title}"


class MatureTalent(OrderMarkerMixin):
    """Третий талант нарабатывается к 40 годам (c)"""

    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="mature_talents"
    )
    title = models.CharField(
        max_length=255,
        verbose_name="Название",
        help_text="Третий талант нарабатывается к 40 годам (c)",
    )
    description = RichTextField(
        verbose_name="Описание", help_text="Третий талант нарабатывается к 40 годам (c)"
    )

    class Meta:
        unique_together = ("category", "order_id")
        verbose_name = "Третий талант нарабатывается к 40 годам"
        verbose_name_plural = "Третий талант нарабатывается к 40 годам"

    def __str__(self):
        return f"{self.category.title} - {self.title}"


# КЕМ РАБОТАТЬ ДЛЯ ДУШИ - soul_work
class InnateTalent(OrderMarkerMixin):
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="innate_talents"
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
        unique_together = ("category", "order_id")
        verbose_name = "Ваш главный талант от рождения"
        verbose_name_plural = "Ваш главный талант от рождения"

    def __str__(self):
        return f"{self.category.title} - {self.title}"


class QualitiesRevealed(OrderMarkerMixin):
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="qualities_revealed"
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
        unique_together = ("category", "order_id")
        verbose_name = "Качества которые раскрываются к 20 годам"
        verbose_name_plural = "Качества которые раскрываются к 20 годам"

    def __str__(self):
        return f"{self.category.title} - {self.title}"


class QualitiesDeveloped(OrderMarkerMixin):
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="qualities_developed"
    )
    title = models.CharField(
        max_length=255,
        verbose_name="Название",
        help_text="Качества которые нарабатываются к 40 годам (c)",
    )
    description = RichTextField(
        verbose_name="Описание",
        help_text="Качества которые нарабатываются к 40 годам (c)",
    )
    

    class Meta:
        unique_together = ("category", "order_id")
        verbose_name = "Качества которые нарабатываются к 40 годам"
        verbose_name_plural = "Качества которые нарабатываются к 40 годам"

    def __str__(self):
        return f"{self.category.title} - {self.title}"


# КАРМА И ЗАДАЧА 40 ЛЕТ - main_task_40
class MainTask40(OrderMarkerMixin):
    """Главная задача 40 лет (d)"""

    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="main_tasks_40"
    )
    title = models.CharField(
        max_length=255, verbose_name="Название", help_text="Главная задача 40 лет (d)"
    )
    description = RichTextField(
        verbose_name="Описание", help_text="Главная задача 40 лет (d)"
    )
    

    class Meta:
        unique_together = ("category", "order_id")
        verbose_name = "Главная задача 40 лет"
        verbose_name_plural = "Главные задачи 40 лет"

    def __str__(self):
        return f"{self.category.title} - {self.title}"


class TaskBefore40(OrderMarkerMixin):
    """Что нужно сделать до 40 лет (d1)"""

    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="tasks_before_40"
    )
    title = models.CharField(
        max_length=255, verbose_name="Название", help_text="Что нужно сделать до 40 лет"
    )
    description = RichTextField(
        verbose_name="Описание", help_text="Что нужно сделать до 40 лет"
    )
    

    class Meta:
        unique_together = ("category", "order_id")
        verbose_name = "Задача до 40 лет"
        verbose_name_plural = "Задачи до 40 лет"

    def __str__(self):
        return f"{self.category.title} - {self.title}"


class TaskAfter40(OrderMarkerMixin):
    """Что нужно сделать после 40 лет (d2)"""

    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="tasks_after_40"
    )
    title = models.CharField(
        max_length=255, verbose_name="Название", help_text="Что нужно сделать до 40 лет"
    )
    description = RichTextField(
        verbose_name="Описание", help_text="Что нужно сделать до 40 лет"
    )
    

    class Meta:
        unique_together = ("category", "order_id")
        verbose_name = "Задача до 40 лет"
        verbose_name_plural = "Задачи до 40 лет"

    def __str__(self):
        return f"{self.category.title} - {self.title}"


# ТОЧКА ДУШЕВНОГО КОМФОРТА - soul_comfort_point
class SoulComfortPoint(OrderMarkerMixin):
    """Точка душевного комфорта (e)"""

    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="soul_comfort_points"
    )
    title = models.CharField(
        max_length=255,
        verbose_name="Название",
        help_text="Точка душевного комфорта (e)",
    )
    description = RichTextField(
        verbose_name="Описание", help_text="Точка душевного комфорта (e)"
    )
    

    class Meta:
        unique_together = ("category", "order_id")
        verbose_name = "Точка душевного комфорта"
        verbose_name_plural = "Точки душевного комфорта"

    def __str__(self):
        return f"{self.category.title} - {self.title}"


# САМОРЕАЛИЗАЦИЯ - self_realization
class SelfRealization(OrderMarkerMixin):
    """Самореализация - Ваша возможность (a2)"""

    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="self_realizations"
    )
    title = models.CharField(
        max_length=255, verbose_name="Название", help_text="Ваша возможность (a2)"
    )
    description = RichTextField(
        verbose_name="Описание", help_text="Ваша возможность (a2)"
    )
    

    class Meta:
        unique_together = ("category", "order_id")
        verbose_name = "Самореализация"
        verbose_name_plural = "Самореализация"

    def __str__(self):
        return f"{self.category.title} - {self.title}"


# ЗАДАЧИ КОТОРЫЕ ТЯНУТСЯ ИЗ ПРОШЛЫХ ЖИЗНЕЙ - past_life_task
class SoulMainTask(OrderMarkerMixin):
    """Главная задача Души (d)"""

    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="soul_main_tasks"
    )
    title = models.CharField(
        max_length=255, verbose_name="Название", help_text="Главная задача Души (d)"
    )
    description = RichTextField(
        verbose_name="Описание", help_text="Главная задача Души (d)"
    )
    

    class Meta:
        unique_together = ("category", "order_id")
        verbose_name = "Главная задача Души"
        verbose_name_plural = "Главные задачи Души"

    def __str__(self):
        return f"{self.category.title} - {self.title}"


class PastLifeExperience(OrderMarkerMixin):
    """Опыт вашей души в прошлом с людьми (d2)"""

    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="past_life_experiences"
    )
    title = models.CharField(
        max_length=255,
        verbose_name="Название",
        help_text="Опыт вашей души в прошлом с людьми (d2)",
    )
    description = RichTextField(
        verbose_name="Описание", help_text="Опыт вашей души в прошлом с людьми (d2)"
    )
    

    class Meta:
        unique_together = ("category", "order_id")
        verbose_name = "Опыт души в прошлом с людьми"
        verbose_name_plural = "Опыт души в прошлом с людьми"

    def __str__(self):
        return f"{self.category.title} - {self.title}"


class PastLifeLesson(OrderMarkerMixin):
    """Урок из прошлой жизни (d1)"""

    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="past_life_lessons"
    )
    title = models.CharField(
        max_length=255, verbose_name="Название", help_text="Урок из прошлой жизни (d1)"
    )
    description = RichTextField(
        verbose_name="Описание", help_text="Урок из прошлой жизни (d1)"
    )
    

    class Meta:
        unique_together = ("category", "order_id")
        verbose_name = "Урок из прошлой жизни"
        verbose_name_plural = "Уроки из прошлой жизни"

    def __str__(self):
        return f"{self.category.title} - {self.title}"


# ТОЧКА ЛИЧНОЙ СИЛЫ - personal_power_point
class PersonalPowerPoint(OrderMarkerMixin):
    """Точка личной силы - Выполняйте рекомендации (e)"""

    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="personal_power_points"
    )
    title = models.CharField(
        max_length=255, verbose_name="Название", help_text="Выполняйте рекомендации (e)"
    )
    description = RichTextField(
        verbose_name="Описание", help_text="Выполняйте рекомендации (e)"
    )
    

    class Meta:
        unique_together = ("category", "order_id")
        verbose_name = "Точка личной силы"
        verbose_name_plural = "Точки личной силы"

    def __str__(self):
        return f"{self.category.title} - {self.title}"


# СИЛА РОДА - ancestral_power
class AncestralPower(OrderMarkerMixin):
    """Сила рода - Необходимо сделать (e1)"""

    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="ancestral_powers"
    )
    title = models.CharField(
        max_length=255, verbose_name="Название", help_text="Необходимо сделать (e1)"
    )
    description = RichTextField(
        verbose_name="Описание", help_text="Необходимо сделать (e1)"
    )
    

    class Meta:
        unique_together = ("category", "order_id")
        verbose_name = "Сила рода"
        verbose_name_plural = "Сила рода"

    def __str__(self):
        return f"{self.category.title} - {self.title}"


# ДЕТСКО-РОДИТЕЛЬСКАЯ КАРМА - parent_child_karma
class TeachParents(OrderMarkerMixin):
    """Чему вы должны были научить своих родителей (a)"""

    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="teach_parents"
    )
    title = models.CharField(
        max_length=255,
        verbose_name="Название",
        help_text="Чему вы должны были научить своих родителей (a)",
    )
    description = RichTextField(
        verbose_name="Описание",
        help_text="Чему вы должны были научить своих родителей (a)",
    )
    

    class Meta:
        unique_together = ("category", "order_id")
        verbose_name = "Чему вы должны были научить родителей"
        verbose_name_plural = "Чему вы должны были научить родителей"

    def __str__(self):
        return f"{self.category.title} - {self.title}"


class RelationshipMistakes(OrderMarkerMixin):
    """Ошибки во взаимоотношениях с родителями и детьми (a2)"""

    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="relationship_mistakes"
    )
    title = models.CharField(
        max_length=255,
        verbose_name="Название",
        help_text="Ошибки во взаимоотношениях с родителями и детьми (a2)",
    )
    description = RichTextField(
        verbose_name="Описание",
        help_text="Ошибки во взаимоотношениях с родителями и детьми (a2)",
    )
    

    class Meta:
        unique_together = ("category", "order_id")
        verbose_name = "Ошибки в отношениях с родителями и детьми"
        verbose_name_plural = "Ошибки в отношениях с родителями и детьми"

    def __str__(self):
        return f"{self.category.title} - {self.title}"


class PersonalGrowth(OrderMarkerMixin):
    """К чему должны прийти, какие качества необходимо в себе наработать (a1)"""

    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="personal_growth"
    )
    title = models.CharField(
        max_length=255,
        verbose_name="Название",
        help_text="К чему должны прийти, какие качества необходимо в себе наработать (a1)",
    )
    description = RichTextField(
        verbose_name="Описание",
        help_text="К чему должны прийти, какие качества необходимо в себе наработать (a1)",
    )
    

    class Meta:
        unique_together = ("category", "order_id")
        verbose_name = "К чему должны прийти"
        verbose_name_plural = "К чему должны прийти"

    def __str__(self):
        return f"{self.category.title} - {self.title}"


# ДУХОВНАЯ КАРМА - spiritual_karma
class SpiritualTask1(OrderMarkerMixin):
    """Духовная карма - Задача 1 (b)"""

    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="spiritual_task_1"
    )
    title = models.CharField(
        max_length=255, verbose_name="Название", help_text="Задача 1 (b)"
    )
    description = RichTextField(
        verbose_name="Описание", help_text="Описание задачи 1 (b)"
    )
    

    class Meta:
        unique_together = ("category", "order_id")
        verbose_name = "Духовная задача 1"
        verbose_name_plural = "Духовные задачи 1"

    def __str__(self):
        return f"{self.category.title} - {self.title}"


class SpiritualTask2(OrderMarkerMixin):
    """Духовная карма - Задача 2 (b1)"""

    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="spiritual_task_2"
    )
    title = models.CharField(
        max_length=255, verbose_name="Название", help_text="Задача 2 (b1)"
    )
    description = RichTextField(
        verbose_name="Описание", help_text="Описание задачи 2 (b1)"
    )
    

    class Meta:
        unique_together = ("category", "order_id")
        verbose_name = "Духовная задача 2"
        verbose_name_plural = "Духовные задачи 2"

    def __str__(self):
        return f"{self.category.title} - {self.title}"


class SpiritualTask3(OrderMarkerMixin):
    """Духовная карма - Задача 3 (b2)"""

    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="spiritual_task_3"
    )
    title = models.CharField(
        max_length=255, verbose_name="Название", help_text="Задача 3 (b2)"
    )
    description = RichTextField(
        verbose_name="Описание", help_text="Описание задачи 3 (b2)"
    )
    

    class Meta:
        unique_together = ("category", "order_id")
        verbose_name = "Духовная задача 3"
        verbose_name_plural = "Духовные задачи 3"

    def __str__(self):
        return f"{self.category.title} - {self.title}"


# ОТНОШЕНИЯ В МАТРИЦЕ - matrix_relationships
class PartnerTasks(OrderMarkerMixin):
    """Какие задачи стоят с партнерами (d2)"""

    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="partner_tasks"
    )
    title = models.CharField(
        max_length=255,
        verbose_name="Название",
        help_text="Какие задачи стоят с партнерами (d2)",
    )
    description = RichTextField(
        verbose_name="Описание", help_text="Какие задачи стоят с партнерами (d2)"
    )
    

    class Meta:
        unique_together = ("category", "order_id")
        verbose_name = "Задачи с партнерами"
        verbose_name_plural = "Задачи с партнерами"

    def __str__(self):
        return f"{self.category.title} - {self.title}"


class SuitablePartner(OrderMarkerMixin):
    """Какой партнер вам подходит (k)"""

    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="suitable_partners"
    )
    title = models.CharField(
        max_length=255,
        verbose_name="Название",
        help_text="Какой партнер вам подходит (k)",
    )
    description = RichTextField(
        verbose_name="Описание", help_text="Какой партнер вам подходит (k)"
    )
    

    class Meta:
        unique_together = ("category", "order_id")
        verbose_name = "Подходящий партнер"
        verbose_name_plural = "Подходящие партнеры"

    def __str__(self):
        return f"{self.category.title} - {self.title}"


class MeetingPlace(OrderMarkerMixin):
    """Где можете познакомиться с партнером (k)"""

    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="meeting_places"
    )
    title = models.CharField(
        max_length=255,
        verbose_name="Название",
        help_text="Где можете познакомиться с партнером (k)",
    )
    description = RichTextField(
        verbose_name="Описание", help_text="Где можете познакомиться с партнером (k)"
    )
    

    class Meta:
        unique_together = ("category", "order_id")
        verbose_name = "Место знакомства с партнером"
        verbose_name_plural = "Места знакомства с партнерами"

    def __str__(self):
        return f"{self.category.title} - {self.title}"


class RelationshipProblems(OrderMarkerMixin):
    """Какие могут возникнуть проблемы в отношениях (j)"""

    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="relationship_problems"
    )
    title = models.CharField(
        max_length=255,
        verbose_name="Название",
        help_text="Какие могут возникнуть проблемы в отношениях (j)",
    )
    description = RichTextField(
        verbose_name="Описание",
        help_text="Какие могут возникнуть проблемы в отношениях (j)",
    )
    

    class Meta:
        unique_together = ("category", "order_id")
        verbose_name = "Проблемы в отношениях"
        verbose_name_plural = "Проблемы в отношениях"

    def __str__(self):
        return f"{self.category.title} - {self.title}"


# ДЕНЬГИ В МАТРИЦЕ - matrix_money
class SuitableProfessions(OrderMarkerMixin):
    """Какие подходят профессии (c2)"""

    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="suitable_professions"
    )
    title = models.CharField(
        max_length=255,
        verbose_name="Название",
        help_text="Какие подходят профессии (c2)",
    )
    description = RichTextField(
        verbose_name="Описание", help_text="Какие подходят профессии (c2)"
    )
    

    class Meta:
        unique_together = ("category", "order_id")
        verbose_name = "Какие подходят профессии"
        verbose_name_plural = "Какие подходят профессии"

    def __str__(self):
        return f"{self.category.title} - {self.title}"


class MoneySources(OrderMarkerMixin):
    """Что дает деньги (l)"""

    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="money_sources"
    )
    title = models.CharField(
        max_length=255, verbose_name="Название", help_text="Что дает деньги (l)"
    )
    description = RichTextField(
        verbose_name="Описание", help_text="Что дает деньги (l)"
    )
    

    class Meta:
        unique_together = ("category", "order_id")
        verbose_name = "Что дает деньги"
        verbose_name_plural = "Что дает деньги"

    def __str__(self):
        return f"{self.category.title} - {self.title}"


class MoneyGrowthTasks1(OrderMarkerMixin):
    """Какие нужно проработать задачи, чтобы раскрыть денежный канал1 (l)"""

    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="money_growth_tasks1"
    )
    title = models.CharField(
        max_length=255,
        verbose_name="Название",
        help_text="Какие нужно проработать задачи, чтобы раскрыть денежный канал1(l)",
    )
    description = RichTextField(
        verbose_name="Описание",
        help_text="Какие нужно проработать задачи, чтобы раскрыть денежный канал1(l)",
    )
    

    class Meta:
        unique_together = ("category", "order_id")
        verbose_name = "Задача для денежного канала1"
        verbose_name_plural = "Задачи для денежного канала1"

    def __str__(self):
        return f"{self.category.title} - {self.title}"


class MoneyGrowthTasks2(OrderMarkerMixin):
    """Какие нужно проработать задачи, чтобы раскрыть денежный канал2 (c2)"""

    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="money_growth_tasks2"
    )
    title = models.CharField(
        max_length=255,
        verbose_name="Название",
        help_text="Какие нужно проработать задачи, чтобы раскрыть денежный канал2(c2)",
    )
    description = RichTextField(
        verbose_name="Описание",
        help_text="Какие нужно проработать задачи, чтобы раскрыть денежный канал2(c2)",
    )
    

    class Meta:
        unique_together = ("category", "order_id")
        verbose_name = "Задача для денежного канала2"
        verbose_name_plural = "Задачи для денежного канала2"

    def __str__(self):
        return f"{self.category.title} - {self.title}"


class MoneyBlocks(OrderMarkerMixin):
    """Что блокирует денежную энергию (j)"""

    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="money_blocks"
    )
    title = models.CharField(
        max_length=255,
        verbose_name="Название",
        help_text="Что блокирует денежную энергию (j)",
    )
    description = RichTextField(
        verbose_name="Описание", help_text="Что блокирует денежную энергию (j)"
    )
    

    class Meta:
        unique_together = ("category", "order_id")
        verbose_name = "Что блокирует денежную энергию"
        verbose_name_plural = "Что блокирует денежную энергию"

    def __str__(self):
        return f"{self.category.title} - {self.title}"


class MoneyUnblock(OrderMarkerMixin):
    """Что помогает раскрыть деньги (j)"""

    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="money_unblock"
    )
    title = models.CharField(
        max_length=255,
        verbose_name="Название",
        help_text="Что помогает раскрыть деньги (j)",
    )
    description = RichTextField(
        verbose_name="Описание", help_text="Что помогает раскрыть деньги (j)"
    )
    

    class Meta:
        unique_together = ("category", "order_id")
        verbose_name = "Что помогает раскрыть деньги"
        verbose_name_plural = "Что помогает раскрыть деньги"

    def __str__(self):
        return f"{self.category.title} - {self.title}"


# ПРЕДНАЗНАЧЕНИЕ - soul_mission
class PersonalPurpose1(OrderMarkerMixin):
    """Задача для персонального 1 Аркана (r)"""

    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="personal_purpose_1"
    )
    title = models.CharField(
        max_length=255,
        verbose_name="Название",
        help_text="Задача для персонального 1 Аркана (r)",
    )
    description = RichTextField(
        verbose_name="Описание",
        help_text="Описание задачи для персонального 1 Аркана (r)",
    )
    

    class Meta:
        unique_together = ("category", "order_id")
        verbose_name = "Персональная задача 1"
        verbose_name_plural = "Персональные задачи 1"

    def __str__(self):
        return f"{self.category.title} - {self.title}"


class PersonalPurpose2(OrderMarkerMixin):
    """Задача для персонального 2 Аркана (s)"""

    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="personal_purpose_2"
    )
    title = models.CharField(
        max_length=255,
        verbose_name="Название",
        help_text="Задача для персонального 2 Аркана (s)",
    )
    description = RichTextField(
        verbose_name="Описание",
        help_text="Описание задачи для персонального 2 Аркана (s)",
    )
    

    class Meta:
        unique_together = ("category", "order_id")
        verbose_name = "Персональная задача 2"
        verbose_name_plural = "Персональные задачи 2"

    def __str__(self):
        return f"{self.category.title} - {self.title}"


class PersonalPurpose3(OrderMarkerMixin):
    """Задача для персонального 3 Аркана (y)"""

    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="personal_purpose_3"
    )
    title = models.CharField(
        max_length=255,
        verbose_name="Название",
        help_text="Задача для персонального 3 Аркана (y)",
    )
    description = RichTextField(
        verbose_name="Описание",
        help_text="Описание задачи для персонального 3 Аркана (y)",
    )
    

    class Meta:
        unique_together = ("category", "order_id")
        verbose_name = "Персональная задача 3"
        verbose_name_plural = "Персональные задачи 3"

    def __str__(self):
        return f"{self.category.title} - {self.title}"


class SocialPurpose1(OrderMarkerMixin):
    """Задача для социального 1 Аркана (t)"""

    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="social_purpose_1"
    )
    title = models.CharField(
        max_length=255,
        verbose_name="Название",
        help_text="Задача для социального 1 Аркана (t)",
    )
    description = RichTextField(
        verbose_name="Описание",
        help_text="Описание задачи для социального 1 Аркана (t)",
    )
    

    class Meta:
        unique_together = ("category", "order_id")
        verbose_name = "Социальная задача 1"
        verbose_name_plural = "Социальные задачи 1"

    def __str__(self):
        return f"{self.category.title} - {self.title}"


class SocialPurpose2(OrderMarkerMixin):
    """Задача для социального 2 Аркана (u)"""

    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="social_purpose_2"
    )
    title = models.CharField(
        max_length=255,
        verbose_name="Название",
        help_text="Задача для социального 2 Аркана (u)",
    )
    description = RichTextField(
        verbose_name="Описание",
        help_text="Описание задачи для социального 2 Аркана (u)",
    )
    

    class Meta:
        unique_together = ("category", "order_id")
        verbose_name = "Социальная задача 2"
        verbose_name_plural = "Социальные задачи 2"

    def __str__(self):
        return f"{self.category.title} - {self.title}"


class SocialPurpose3(OrderMarkerMixin):
    """Задача для социального 3 Аркана (v)"""

    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="social_purpose_3"
    )
    title = models.CharField(
        max_length=255,
        verbose_name="Название",
        help_text="Задача для социального 3 Аркана (v)",
    )
    description = RichTextField(
        verbose_name="Описание",
        help_text="Описание задачи для социального 3 Аркана (v)",
    )
    

    class Meta:
        unique_together = ("category", "order_id")
        verbose_name = "Социальная задача 3"
        verbose_name_plural = "Социальные задачи 3"

    def __str__(self):
        return f"{self.category.title} - {self.title}"


class SpiritualPurpose(OrderMarkerMixin):
    """Духовное предназначение (w)"""

    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="spiritual_purpose"
    )
    title = models.CharField(
        max_length=255, verbose_name="Название", help_text="Духовное предназначение (w)"
    )
    description = RichTextField(
        verbose_name="Описание", help_text="Духовное предназначение (w)"
    )
    

    class Meta:
        unique_together = ("category", "order_id")
        verbose_name = "Духовное предназначение"
        verbose_name_plural = "Духовные предназначения"

    def __str__(self):
        return f"{self.category.title} - {self.title}"


# ПРЕДРАСПОЛОЖЕННОСТЬ К ЗАБОЛЕВАНИЯМ - disease_predisposition
class PaternalDiseases(OrderMarkerMixin):
    """Родовые заболевания по линии отца (h)"""

    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="paternal_diseases"
    )
    title = models.CharField(
        max_length=255,
        verbose_name="Название",
        help_text="Родовые заболевания по линии отца (h)",
    )
    description = RichTextField(
        verbose_name="Описание", help_text="Родовые заболевания по линии отца (h)"
    )
    

    class Meta:
        unique_together = ("category", "order_id")
        verbose_name = "Родовое заболевание по линии отца"
        verbose_name_plural = "Родовые заболевания по линии отца"

    def __str__(self):
        return f"{self.category.title} - {self.title}"


class MaternalDiseases(OrderMarkerMixin):
    """Родовые заболевания по линии матери (i)"""

    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="maternal_diseases"
    )
    title = models.CharField(
        max_length=255,
        verbose_name="Название",
        help_text="Родовые заболевания по линии матери (i)",
    )
    description = RichTextField(
        verbose_name="Описание", help_text="Родовые заболевания по линии матери (i)"
    )
    

    class Meta:
        unique_together = ("category", "order_id")
        verbose_name = "Родовое заболевание по линии матери"
        verbose_name_plural = "Родовые заболевания по линии матери"

    def __str__(self):
        return f"{self.category.title} - {self.title}"


class HealthArcane1(OrderMarkerMixin):
    """Предрасположенность к заболеваниям по арканам1 (a)"""

    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="health_arcane1"
    )
    title = models.CharField(
        max_length=255,
        verbose_name="Название",
        help_text="Предрасположенность к заболеваниям(a)",
    )
    description = RichTextField(
        verbose_name="Описание",
        help_text="Описание предрасположенности к заболеваниям(a)",
    )
    

    class Meta:
        unique_together = ("category", "order_id")
        verbose_name = "Предрасположенность к заболеваниям1"
        verbose_name_plural = "Предрасположенности к заболеваниям1"

    def __str__(self):
        return f"{self.category.title} - {self.title}"


class HealthArcane2(OrderMarkerMixin):
    """Предрасположенность к заболеваниям по арканам2 (b)"""

    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="health_arcane2"
    )
    title = models.CharField(
        max_length=255,
        verbose_name="Название",
        help_text="Предрасположенность к заболеваниям(b)",
    )
    description = RichTextField(
        verbose_name="Описание",
        help_text="Описание предрасположенности к заболеваниям(b)",
    )
    

    class Meta:
        unique_together = ("category", "order_id")
        verbose_name = "Предрасположенность к заболеваниям2"
        verbose_name_plural = "Предрасположенности к заболеваниям2"

    def __str__(self):
        return f"{self.category.title} - {self.title}"


class HealthArcane3(OrderMarkerMixin):
    """Предрасположенность к заболеваниям по арканам3 (c)"""

    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="health_arcane3"
    )
    title = models.CharField(
        max_length=255,
        verbose_name="Название",
        help_text="Предрасположенность к заболеваниям(c)",
    )
    description = RichTextField(
        verbose_name="Описание",
        help_text="Описание предрасположенности к заболеваниям(c)",
    )
    

    class Meta:
        unique_together = ("category", "order_id")
        verbose_name = "Предрасположенность к заболеваниям3"
        verbose_name_plural = "Предрасположенности к заболеваниям3"

    def __str__(self):
        return f"{self.category.title} - {self.title}"


# ЗАДАЧИ РОДА ДО 7 КОЛЕНА - AncestralTask7
class AncestralTaskFatherMale(OrderMarkerMixin):
    """Задачи по мужской линии по роду отца (f)"""

    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="ancestral_tasks_father_male"
    )
    title = models.CharField(
        max_length=255,
        verbose_name="Название",
        help_text="Задачи по мужской линии по роду отца (f)",
    )
    description = RichTextField(
        verbose_name="Описание",
        help_text="Описание задач по мужской линии по роду отца (f)",
    )
    

    class Meta:
        unique_together = ("category", "order_id")
        verbose_name = "Задача по мужской линии отца"
        verbose_name_plural = "Задачи по мужской линии отца"

    def __str__(self):
        return f"{self.category.title} - {self.title}"


class AncestralTaskMotherMale(OrderMarkerMixin):
    """Задачи по мужской линии по роду матери (h)"""

    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="ancestral_tasks_mother_male"
    )
    title = models.CharField(
        max_length=255,
        verbose_name="Название",
        help_text="Задачи по мужской линии по роду матери (h)",
    )
    description = RichTextField(
        verbose_name="Описание",
        help_text="Описание задач по мужской линии по роду матери (h)",
    )
    

    class Meta:
        unique_together = ("category", "order_id")
        verbose_name = "Задача по мужской линии матери"
        verbose_name_plural = "Задачи по мужской линии матери"

    def __str__(self):
        return f"{self.category.title} - {self.title}"


class AncestralTaskFatherFemale(OrderMarkerMixin):
    """Задачи по женской линии по роду отца (g)"""

    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="ancestral_tasks_father_female"
    )
    title = models.CharField(
        max_length=255,
        verbose_name="Название",
        help_text="Задачи по женской линии по роду отца (g)",
    )
    description = RichTextField(
        verbose_name="Описание",
        help_text="Описание задач по женской линии по роду отца (g)",
    )
    

    class Meta:
        unique_together = ("category", "order_id")
        verbose_name = "Задача по женской линии отца"
        verbose_name_plural = "Задачи по женской линии отца"

    def __str__(self):
        return f"{self.category.title} - {self.title}"


class AncestralTaskMotherFemale(OrderMarkerMixin):
    """Задачи по женской линии по роду матери (i)"""

    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="ancestral_tasks_mother_female"
    )
    title = models.CharField(
        max_length=255,
        verbose_name="Название",
        help_text="Задачи по женской линии по роду матери (i)",
    )
    description = RichTextField(
        verbose_name="Описание",
        help_text="Описание задач по женской линии по роду матери (i)",
    )
    

    class Meta:
        unique_together = ("category", "order_id")
        verbose_name = "Задача по женской линии матери"
        verbose_name_plural = "Задачи по женской линии матери"

    def __str__(self):
        return f"{self.category.title} - {self.title}"


# КАРТА ЗДОРОВЬЯ - health_map

# Sahasrara
class SahasraraO7(OrderMarkerMixin):
    """Карта здоровья аркан SahasraraO7"""

    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="sahasrara_o7"
    )
    title = models.CharField(
        max_length=255,
        verbose_name="Название",
        help_text="Карта здоровья аркан SahasraraO7",
    )
    description = RichTextField(
        verbose_name="Описание", help_text="Карта здоровья аркан SahasraraO7"
    )
    

    class Meta:
        verbose_name = "Карта здоровья аркан SahasraraO7"
        verbose_name_plural = "Карта здоровья аркан SahasraraO7"
        unique_together = ("category", "order_id")

    def __str__(self):
        return f"{self.category.title} - {self.title}"


class SahasraraP7(OrderMarkerMixin):
    """Карта здоровья аркан SahasraraP7"""

    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="sahasrara_p7"
    )
    title = models.CharField(
        max_length=255,
        verbose_name="Название",
        help_text="Карта здоровья аркан SahasraraP7",
    )
    description = RichTextField(
        verbose_name="Описание", help_text="Карта здоровья аркан SahasraraP7"
    )
    

    class Meta:
        verbose_name = "Карта здоровья аркан SahasraraP7"
        verbose_name_plural = "Карта здоровья аркан SahasraraP7"
        unique_together = ("category", "order_id")

    def __str__(self):
        return f"{self.category.title} - {self.title}"


class SahasraraQ7(OrderMarkerMixin):
    """Карта здоровья аркан SahasraraQ7"""

    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="sahasrara_q7"
    )
    title = models.CharField(
        max_length=255,
        verbose_name="Название",
        help_text="Карта здоровья аркан SahasraraQ7",
    )
    description = RichTextField(
        verbose_name="Описание", help_text="Карта здоровья аркан SahasraraQ7"
    )
    

    class Meta:
        verbose_name = "Карта здоровья аркан SahasraraQ7"
        verbose_name_plural = "Карта здоровья аркан SahasraraQ7"
        unique_together = ("category", "order_id")

    def __str__(self):
        return f"{self.category.title} - {self.title}"


# Adjna
class AdjnaO6(OrderMarkerMixin):
    """Карта здоровья аркан AdjnaO6"""

    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="adjna_o6"
    )
    title = models.CharField(
        max_length=255,
        verbose_name="Название",
        help_text="Карта здоровья аркан AdjnaO6",
    )
    description = RichTextField(
        verbose_name="Описание", help_text="Карта здоровья аркан AdjnaO6"
    )
    

    class Meta:
        verbose_name = "Карта здоровья аркан AdjnaO6"
        verbose_name_plural = "Карта здоровья аркан AdjnaO6"
        unique_together = ("category", "order_id")

    def __str__(self):
        return f"{self.category.title} - {self.title}"


class AdjnaP6(OrderMarkerMixin):
    """Карта здоровья аркан AdjnaP6"""

    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="adjna_p6"
    )
    title = models.CharField(
        max_length=255,
        verbose_name="Название",
        help_text="Карта здоровья аркан AdjnaP6",
    )
    description = RichTextField(
        verbose_name="Описание", help_text="Карта здоровья аркан AdjnaP6"
    )
    

    class Meta:
        verbose_name = "Карта здоровья аркан AdjnaP6"
        verbose_name_plural = "Карта здоровья аркан AdjnaP6"
        unique_together = ("category", "order_id")

    def __str__(self):
        return f"{self.category.title} - {self.title}"


class AdjnaQ6(OrderMarkerMixin):
    """Карта здоровья аркан AdjnaQ6"""

    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="adjna_q6"
    )
    title = models.CharField(
        max_length=255,
        verbose_name="Название",
        help_text="Карта здоровья аркан AdjnaQ6",
    )
    description = RichTextField(
        verbose_name="Описание", help_text="Карта здоровья аркан AdjnaQ6"
    )
    

    class Meta:
        verbose_name = "Карта здоровья аркан AdjnaQ6"
        verbose_name_plural = "Карта здоровья аркан AdjnaQ6"
        unique_together = ("category", "order_id")

    def __str__(self):
        return f"{self.category.title} - {self.title}"


# Vishudkha
class VishudkhaO5(OrderMarkerMixin):
    """Карта здоровья аркан VishudkhaO5"""

    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="vishudkha_o5"
    )
    title = models.CharField(
        max_length=255,
        verbose_name="Название",
        help_text="Карта здоровья аркан VishudkhaO5",
    )
    description = RichTextField(
        verbose_name="Описание", help_text="Карта здоровья аркан VishudkhaO5"
    )
    

    class Meta:
        verbose_name = "Карта здоровья аркан VishudkhaO5"
        verbose_name_plural = "Карта здоровья аркан VishudkhaO5"
        unique_together = ("category", "order_id")

    def __str__(self):
        return f"{self.category.title} - {self.title}"


class VishudkhaP5(OrderMarkerMixin):
    """Карта здоровья аркан VishudkhaP5"""

    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="vishudkha_p5"
    )
    title = models.CharField(
        max_length=255,
        verbose_name="Название",
        help_text="Карта здоровья аркан VishudkhaP5",
    )
    description = RichTextField(
        verbose_name="Описание", help_text="Карта здоровья аркан VishudkhaP5"
    )
    

    class Meta:
        verbose_name = "Карта здоровья аркан VishudkhaP5"
        verbose_name_plural = "Карта здоровья аркан VishudkhaP5"
        unique_together = ("category", "order_id")

    def __str__(self):
        return f"{self.category.title} - {self.title}"


class VishudkhaQ5(OrderMarkerMixin):
    """Карта здоровья аркан VishudkhaQ5"""

    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="vishudkha_q5"
    )
    title = models.CharField(
        max_length=255,
        verbose_name="Название",
        help_text="Карта здоровья аркан VishudkhaQ5",
    )
    description = RichTextField(
        verbose_name="Описание", help_text="Карта здоровья аркан VishudkhaQ5"
    )
    

    class Meta:
        verbose_name = "Карта здоровья аркан VishudkhaQ5"
        verbose_name_plural = "Карта здоровья аркан VishudkhaQ5"
        unique_together = ("category", "order_id")

    def __str__(self):
        return f"{self.category.title} - {self.title}"


# Anakhata
class AnakhataO4(OrderMarkerMixin):
    """Карта здоровья аркан AnakhataO4"""

    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="anakhata_o4"
    )
    title = models.CharField(
        max_length=255,
        verbose_name="Название",
        help_text="Карта здоровья аркан AnakhataO4",
    )
    description = RichTextField(
        verbose_name="Описание", help_text="Карта здоровья аркан AnakhataO4"
    )
    

    class Meta:
        verbose_name = "Карта здоровья аркан AnakhataO4"
        verbose_name_plural = "Карта здоровья аркан AnakhataO4"
        unique_together = ("category", "order_id")

    def __str__(self):
        return f"{self.category.title} - {self.title}"


class AnakhataP4(OrderMarkerMixin):
    """Карта здоровья аркан AnakhataP4"""

    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="anakhata_p4"
    )
    title = models.CharField(
        max_length=255,
        verbose_name="Название",
        help_text="Карта здоровья аркан AnakhataP4",
    )
    description = RichTextField(
        verbose_name="Описание", help_text="Карта здоровья аркан AnakhataP4"
    )
    

    class Meta:
        verbose_name = "Карта здоровья аркан AnakhataP4"
        verbose_name_plural = "Карта здоровья аркан AnakhataP4"
        unique_together = ("category", "order_id")

    def __str__(self):
        return f"{self.category.title} - {self.title}"


class AnakhataQ4(OrderMarkerMixin):
    """Карта здоровья аркан AnakhataQ4"""

    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="anakhata_q4"
    )
    title = models.CharField(
        max_length=255,
        verbose_name="Название",
        help_text="Карта здоровья аркан AnakhataQ4",
    )
    description = RichTextField(
        verbose_name="Описание", help_text="Карта здоровья аркан AnakhataQ4"
    )
    

    class Meta:
        verbose_name = "Карта здоровья аркан AnakhataQ4"
        verbose_name_plural = "Карта здоровья аркан AnakhataQ4"
        unique_together = ("category", "order_id")

    def __str__(self):
        return f"{self.category.title} - {self.title}"


# Manipura
class ManipuraO3(OrderMarkerMixin):
    """Карта здоровья аркан ManipuraO3"""

    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="manipura_o3"
    )
    title = models.CharField(
        max_length=255,
        verbose_name="Название",
        help_text="Карта здоровья аркан ManipuraO3",
    )
    description = RichTextField(
        verbose_name="Описание", help_text="Карта здоровья аркан ManipuraO3"
    )
    

    class Meta:
        verbose_name = "Карта здоровья аркан ManipuraO3"
        verbose_name_plural = "Карта здоровья аркан ManipuraO3"
        unique_together = ("category", "order_id")

    def __str__(self):
        return f"{self.category.title} - {self.title}"


class ManipuraP3(OrderMarkerMixin):
    """Карта здоровья аркан ManipuraP3"""

    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="manipura_p3"
    )
    title = models.CharField(
        max_length=255,
        verbose_name="Название",
        help_text="Карта здоровья аркан ManipuraP3",
    )
    description = RichTextField(
        verbose_name="Описание", help_text="Карта здоровья аркан ManipuraP3"
    )
    

    class Meta:
        verbose_name = "Карта здоровья аркан ManipuraP3"
        verbose_name_plural = "Карта здоровья аркан ManipuraP3"
        unique_together = ("category", "order_id")

    def __str__(self):
        return f"{self.category.title} - {self.title}"


class ManipuraQ3(OrderMarkerMixin):
    """Карта здоровья аркан ManipuraQ3"""

    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="manipura_q3"
    )
    title = models.CharField(
        max_length=255,
        verbose_name="Название",
        help_text="Карта здоровья аркан ManipuraQ3",
    )
    description = RichTextField(
        verbose_name="Описание", help_text="Карта здоровья аркан ManipuraQ3"
    )
    

    class Meta:
        verbose_name = "Карта здоровья аркан ManipuraQ3"
        verbose_name_plural = "Карта здоровья аркан ManipuraQ3"
        unique_together = ("category", "order_id")

    def __str__(self):
        return f"{self.category.title} - {self.title}"


# Svadkhistana
class SvadkhistanaO2(OrderMarkerMixin):
    """Карта здоровья аркан SvadkhistanaO2"""

    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="svadkhistana_o2"
    )
    title = models.CharField(
        max_length=255,
        verbose_name="Название",
        help_text="Карта здоровья аркан SvadkhistanaO2",
    )
    description = RichTextField(
        verbose_name="Описание", help_text="Карта здоровья аркан SvadkhistanaO2"
    )
    

    class Meta:
        verbose_name = "Карта здоровья аркан SvadkhistanaO2"
        verbose_name_plural = "Карта здоровья аркан SvadkhistanaO2"
        unique_together = ("category", "order_id")

    def __str__(self):
        return f"{self.category.title} - {self.title}"


class SvadkhistanaP2(OrderMarkerMixin):
    """Карта здоровья аркан SvadkhistanaP2"""

    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="svadkhistana_p2"
    )
    title = models.CharField(
        max_length=255,
        verbose_name="Название",
        help_text="Карта здоровья аркан SvadkhistanaP2",
    )
    description = RichTextField(
        verbose_name="Описание", help_text="Карта здоровья аркан SvadkhistanaP2"
    )
    

    class Meta:
        verbose_name = "Карта здоровья аркан SvadkhistanaP2"
        verbose_name_plural = "Карта здоровья аркан SvadkhistanaP2"
        unique_together = ("category", "order_id")

    def __str__(self):
        return f"{self.category.title} - {self.title}"


class SvadkhistanaQ2(OrderMarkerMixin):
    """Карта здоровья аркан SvadkhistanaQ2"""

    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="svadkhistana_q2"
    )
    title = models.CharField(
        max_length=255,
        verbose_name="Название",
        help_text="Карта здоровья аркан SvadkhistanaQ2",
    )
    description = RichTextField(
        verbose_name="Описание", help_text="Карта здоровья аркан SvadkhistanaQ2"
    )
    

    class Meta:
        verbose_name = "Карта здоровья аркан SvadkhistanaQ2"
        verbose_name_plural = "Карта здоровья аркан SvadkhistanaQ2"
        unique_together = ("category", "order_id")

    def __str__(self):
        return f"{self.category.title} - {self.title}"


# Muladkhara
class MuladkharaO1(OrderMarkerMixin):
    """Карта здоровья аркан Muladkhara1"""

    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="muladkhara_o1"
    )
    title = models.CharField(
        max_length=255,
        verbose_name="Название",
        help_text="Карта здоровья аркан Muladkhara1",
    )
    description = RichTextField(
        verbose_name="Описание", help_text="Карта здоровья аркан Muladkhara1"
    )
    

    class Meta:
        verbose_name = "Карта здоровья аркан Muladkhara1"
        verbose_name_plural = "Карта здоровья аркан Muladkhara1"
        unique_together = ("category", "order_id")

    def __str__(self):
        return f"{self.category.title} - {self.title}"


class MuladkharaP1(OrderMarkerMixin):
    """Карта здоровья аркан MuladkharaP1"""

    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="muladkhara_p1"
    )
    title = models.CharField(
        max_length=255,
        verbose_name="Название",
        help_text="Карта здоровья аркан MuladkharaP1",
    )
    description = RichTextField(
        verbose_name="Описание", help_text="Карта здоровья аркан MuladkharaP1"
    )
    

    class Meta:
        verbose_name = "Карта здоровья аркан MuladkharaP1"
        verbose_name_plural = "Карта здоровья аркан MuladkharaP1"
        unique_together = ("category", "order_id")

    def __str__(self):
        return f"{self.category.title} - {self.title}"


class MuladkharaQ1(OrderMarkerMixin):
    """Карта здоровья аркан MuladkharaQ1"""

    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="muladkhara_q1"
    )
    title = models.CharField(
        max_length=255,
        verbose_name="Название",
        help_text="Карта здоровья аркан MuladkharaQ1",
    )
    description = RichTextField(
        verbose_name="Описание", help_text="Карта здоровья аркан MuladkharaQ1"
    )
    

    class Meta:
        verbose_name = "Карта здоровья аркан MuladkharaQ1"
        verbose_name_plural = "Карта здоровья аркан MuladkharaQ1"
        unique_together = ("category", "order_id")

    def __str__(self):
        return f"{self.category.title} - {self.title}"


# Total
class TotalO(OrderMarkerMixin):
    """Карта здоровья аркан TotalO"""

    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="total_o"
    )
    title = models.CharField(
        max_length=255, verbose_name="Название", help_text="Карта здоровья аркан TotalO"
    )
    description = RichTextField(
        verbose_name="Описание", help_text="Карта здоровья аркан TotalO"
    )
    

    class Meta:
        verbose_name = "Карта здоровья аркан TotalO"
        verbose_name_plural = "Карта здоровья аркан TotalO"
        unique_together = ("category", "order_id")

    def __str__(self):
        return f"{self.category.title} - {self.title}"


class TotalP(OrderMarkerMixin):
    """Карта здоровья аркан TotalP"""

    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="total_p"
    )
    title = models.CharField(
        max_length=255, verbose_name="Название", help_text="Карта здоровья аркан TotalP"
    )
    description = RichTextField(
        verbose_name="Описание", help_text="Карта здоровья аркан TotalP"
    )
    

    class Meta:
        verbose_name = "Карта здоровья аркан TotalP"
        verbose_name_plural = "Карта здоровья аркан TotalP"
        unique_together = ("category", "order_id")

    def __str__(self):
        return f"{self.category.title} - {self.title}"


class TotalQ(OrderMarkerMixin):
    """Карта здоровья аркан TotalQ"""

    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="total_q"
    )
    title = models.CharField(
        max_length=255, verbose_name="Название", help_text="Карта здоровья аркан TotalQ"
    )
    description = RichTextField(
        verbose_name="Описание", help_text="Карта здоровья аркан TotalQ"
    )
    

    class Meta:
        verbose_name = "Карта здоровья аркан TotalQ"
        verbose_name_plural = "Карта здоровья аркан TotalQ"
        unique_together = ("category", "order_id")

    def __str__(self):
        return f"{self.category.title} - {self.title}"


class MatrixFateProgram(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name="Название программы"
    )

    marker_1_name = models.CharField(
        max_length=3,
        verbose_name="Маркер 1",
        help_text="Пример: a, a1, a2"
    )
    marker_1_value = models.IntegerField(
        verbose_name="Значение маркера 1",
        help_text="Значение от 1 до 22",
        choices=[(i, i) for i in range(1, 23)]
    )

    marker_2_name = models.CharField(
        max_length=3,
        verbose_name="Маркер 2",
        help_text="Пример: b, b1, b2"
    )
    marker_2_value = models.IntegerField(
        verbose_name="Значение маркера 2",
        help_text="Значение от 1 до 22",
        choices=[(i, i) for i in range(1, 23)]
    )

    marker_3_name = models.CharField(
        max_length=3,
        verbose_name="Маркер 3",
        help_text="Пример: m, n, c2"
    )
    marker_3_value = models.IntegerField(
        verbose_name="Значение маркера 3",
        help_text="Значение от 1 до 22",
        choices=[(i, i) for i in range(1, 23)]
    )

    description = RichTextField(
        blank=True,
        verbose_name="Описание программы"
    )

    class Meta:
        verbose_name = "Программа Матрицы судьбы"
        verbose_name_plural = "Программы Матрицы судьбы"

    def __str__(self):
        return self.name
