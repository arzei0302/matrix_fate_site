from django.db import models, transaction
from ckeditor.fields import RichTextField
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db.models import Max


class AccessMatrixModel(models.Model):
    """Таблица доступов"""
    name = models.CharField(max_length=255, verbose_name="Название")
    description = RichTextField(verbose_name="Описание")
    is_active = models.BooleanField(default=True, verbose_name="Активен")
    order = models.PositiveSmallIntegerField(verbose_name="Порядковый номер", blank=True, null=True)

    class Meta:
        verbose_name = "Таблица доступов"
        verbose_name_plural = "Таблицы доступов"

    def save(self, *args, **kwargs):
        if self.order is None:
            with transaction.atomic():
                max_order = self.__class__.objects.filter().aggregate(max_order=Max("order"))["max_order"]
                self.order = (max_order or 0) + 1
        super().save(*args, **kwargs)


# ADDITIONAL CALC MODELS

class FinancialAndAntiCodeCalculation(models.Model):
    """Калькуляция финансов и антикодов"""
    title = models.CharField(max_length=255, verbose_name="Название")
    description = RichTextField(verbose_name="Описание")
    order_id = models.PositiveSmallIntegerField(
        verbose_name="№ аркана",
        validators=[MinValueValidator(1), MaxValueValidator(22)],
    )
    image = models.ImageField(upload_to='financial_and_anti_code_calculations/', verbose_name="Изображение")

    class Meta:
        verbose_name = "Калькуляция финансов и антикодов"
        verbose_name_plural = "Калькуляции финансов и антикодов"

    def __str__(self):
        return self.title


class ArcanaClues(models.Model):
    """Подсказка арканов"""
    title = models.CharField(max_length=255, verbose_name="Название")
    description = RichTextField(verbose_name="Описание")
    image = models.ImageField(upload_to='arcana_clues/', verbose_name="Изображение")

    class Meta:
        verbose_name = "Подсказка арканов"
        verbose_name_plural = "Подсказки арканов"

    def __str__(self):
        return self.title


class PastCard(models.Model):
    """Карта Прошлое"""
    title = models.CharField(max_length=255, verbose_name="Название (Прошлое)")
    description = RichTextField(verbose_name="Описание")
    image = models.ImageField(upload_to='past_cards/', verbose_name="Изображение")

    class Meta:
        verbose_name = "Карта Прошлое"
        verbose_name_plural = "Карты Прошлое"

    def __str__(self):
        return self.title

class PresentCard(models.Model):
    """Карта Настоящее"""
    title = models.CharField(max_length=255, verbose_name="Название (Настоящее)")
    description = RichTextField(verbose_name="Описание")
    image = models.ImageField(upload_to='present_cards/', verbose_name="Изображение")

    class Meta:
        verbose_name = "Карта Настоящее"
        verbose_name_plural = "Карты Настоящее"

    def __str__(self):
        return self.title

class FutureCard(models.Model):
    """Карта Будущее"""
    title = models.CharField(max_length=255, verbose_name="Название (Будущее)")
    description = RichTextField(verbose_name="Описание")
    image = models.ImageField(upload_to='future_cards/', verbose_name="Изображение")

    class Meta:
        verbose_name = "Карта Будущее"
        verbose_name_plural = "Карты Будущее"

    def __str__(self):
        return self.title


# FOOTER MODELS
class SingleInstanceModel(models.Model):
    """Абстрактная модель для ограничения одной записью"""
    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if not self.pk and self.__class__.objects.exists():
            raise ValueError(f"Добавление более одной записи запрещено для {self.__class__.__name__}.")
        super().save(*args, **kwargs)

class SingleInstanceModel(models.Model):
    """Абстрактная модель для ограничения одной записью"""

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if not self.pk and self.__class__.objects.exists():
            existing_instance = self.__class__.objects.first()
            self.pk = existing_instance.pk  # Перезаписываем существующую запись
        super().save(*args, **kwargs)


class MessageSupport(models.Model):
    """Модель Написать в поддержку"""
    title = models.CharField(max_length=255, verbose_name="Название")
    description = RichTextField(verbose_name="Описание")
    reference = models.CharField(max_length=255, verbose_name="Ссылка")

    class Meta:
        verbose_name = "Написать в поддержку"
        verbose_name_plural = "Написать в поддержку"


class PublicOfferAgreement(models.Model):
    """Модель Договор публичной оферты"""
    title = models.CharField(max_length=255, verbose_name="Название")
    description = RichTextField(verbose_name="Описание")

    class Meta:
        verbose_name = "Публичное предложение"
        verbose_name_plural = "Публичное предложение"


class PrivacyPolicy(models.Model):
    """Модель Политика конфиденциальности"""
    title = models.CharField(max_length=255, verbose_name="Название")
    description = RichTextField(verbose_name="Описание")

    class Meta:
        verbose_name = "Политика конфиденциальности"
        verbose_name_plural = "Политика конфиденциальности"


# BANNERS
class LandingPage(models.Model):
    """Баннеры и лендинги главной странице"""
    title = models.CharField(max_length=255, verbose_name="Название")
    sub_title = models.CharField(max_length=255, verbose_name="Подзаголовок")
    description = RichTextField(verbose_name="Описание")
    sub_description = RichTextField(verbose_name="Подописание")
    order_id = models.PositiveSmallIntegerField()
    reference1 = models.CharField(max_length=255, verbose_name="Ссылка")
    reference2 = models.CharField(max_length=255, verbose_name="Ссылка")
    image1 = models.ImageField(upload_to='landing_page/', verbose_name="Изображение1")
    image2 = models.ImageField(upload_to='landing_page/', verbose_name="Изображение2")
    image3 = models.ImageField(upload_to='landing_page/', verbose_name="Изображение3")
    image4 = models.ImageField(upload_to='landing_page/', verbose_name="Изображение4")
    image5 = models.ImageField(upload_to='landing_page/', verbose_name="Изображение5")

    class Meta:
        verbose_name = "Баннер/Лендинг"
        verbose_name_plural = "Баннеры/Лендинги"

    def __str__(self):
        return self.title
    

# Модель для ссылок на соц. сети
class SocialLinks(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название")
    link = models.URLField(verbose_name="Ссылка")

    class Meta:
        verbose_name = "Ссылка на соц. сеть"
        verbose_name_plural = "Ссылки на соц. сети"

    def __str__(self):
        return self.title