from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from ckeditor.fields import RichTextField


class GeneralPrognosis(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название", help_text="Общий прогноз")
    description = RichTextField(verbose_name="Описание", help_text="Общий прогноз")
    order_id = models.PositiveSmallIntegerField(
        verbose_name="№ аркана",
        validators=[MinValueValidator(1), MaxValueValidator(22)],
    )
    class Meta:
        verbose_name = "Общий прогноз"
        verbose_name_plural = "Общий прогноз"

    def __str__(self):
        return self.title
    

class January(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название", help_text="Январь")
    description = RichTextField(verbose_name="Описание", help_text="Январь")
    order_id = models.PositiveSmallIntegerField(
        verbose_name="№ аркана",
        validators=[MinValueValidator(1), MaxValueValidator(22)],
    )
    class Meta:
        verbose_name = "Январь"
        verbose_name_plural = "Январь"

    def __str__(self):
        return self.title
    

class February(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название", help_text="Февраль")
    description = RichTextField(verbose_name="Описание", help_text="Февраль")
    order_id = models.PositiveSmallIntegerField(
        verbose_name="№ аркана",
        validators=[MinValueValidator(1), MaxValueValidator(22)],
    )
    class Meta:
        verbose_name = "Февраль"
        verbose_name_plural = "Февраль"

    def __str__(self):
        return self.title
    

class March(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название", help_text="Март")
    description = RichTextField(verbose_name="Описание", help_text="Март")
    order_id = models.PositiveSmallIntegerField(
        verbose_name="№ аркана",
        validators=[MinValueValidator(1), MaxValueValidator(22)],
    )
    class Meta:
        verbose_name = "Март"
        verbose_name_plural = "Март"

    def __str__(self):
        return self.title
    

class April(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название", help_text="Апрель")
    description = RichTextField(verbose_name="Описание", help_text="Апрель")
    order_id = models.PositiveSmallIntegerField(
        verbose_name="№ аркана",
        validators=[MinValueValidator(1), MaxValueValidator(22)],
    )
    class Meta:
        verbose_name = "Апрель"
        verbose_name_plural = "Апрель"

    def __str__(self):
        return self.title
    

class May(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название", help_text="Май")
    description = RichTextField(verbose_name="Описание", help_text="Май")
    order_id = models.PositiveSmallIntegerField(
        verbose_name="№ аркана",
        validators=[MinValueValidator(1), MaxValueValidator(22)],
    )
    class Meta:
        verbose_name = "Май"
        verbose_name_plural = "Май"

    def __str__(self):
        return self.title
    

class June(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название", help_text="Июнь")
    description = RichTextField(verbose_name="Описание", help_text="Июнь")
    order_id = models.PositiveSmallIntegerField(
        verbose_name="№ аркана",
        validators=[MinValueValidator(1), MaxValueValidator(22)],
    )
    class Meta:
        verbose_name = "Июнь"
        verbose_name_plural = "Июнь"

    def __str__(self):
        return self.title
    

class July(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название", help_text="Июль")
    description = RichTextField(verbose_name="Описание", help_text="Июль")
    order_id = models.PositiveSmallIntegerField(
        verbose_name="№ аркана",
        validators=[MinValueValidator(1), MaxValueValidator(22)],
    )
    class Meta:
        verbose_name = "Июль"
        verbose_name_plural = "Июль"

    def __str__(self):
        return self.title
    

class August(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название", help_text="Август")
    description = RichTextField(verbose_name="Описание", help_text="Август")
    order_id = models.PositiveSmallIntegerField(
        verbose_name="№ аркана",
        validators=[MinValueValidator(1), MaxValueValidator(22)],
    )
    class Meta:
        verbose_name = "Август"
        verbose_name_plural = "Август"

    def __str__(self):
        return self.title
    

class September(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название", help_text="Сентябрь")
    description = RichTextField(verbose_name="Описание", help_text="Сентябрь")
    order_id = models.PositiveSmallIntegerField(
        verbose_name="№ аркана",
        validators=[MinValueValidator(1), MaxValueValidator(22)],
    )
    class Meta:
        verbose_name = "Сентябрь"
        verbose_name_plural = "Сентябрь"

    def __str__(self):
        return self.title
    

class October(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название", help_text="Октябрь")
    description = RichTextField(verbose_name="Описание", help_text="Октябрь")
    order_id = models.PositiveSmallIntegerField(
        verbose_name="№ аркана",
        validators=[MinValueValidator(1), MaxValueValidator(22)],
    )
    class Meta:
        verbose_name = "Октябрь"
        verbose_name_plural = "Октябрь"

    def __str__(self):
        return self.title
    

class November(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название", help_text="Ноябрь")
    description = RichTextField(verbose_name="Описание", help_text="Ноябрь")
    order_id = models.PositiveSmallIntegerField(
        verbose_name="№ аркана",
        validators=[MinValueValidator(1), MaxValueValidator(22)],
    )
    class Meta:
        verbose_name = "Ноябрь"
        verbose_name_plural = "Ноябрь"

    def __str__(self):
        return self.title
    

class December(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название", help_text="Декабрь")
    description = RichTextField(verbose_name="Описание", help_text="Декабрь")
    order_id = models.PositiveSmallIntegerField(
        verbose_name="№ аркана",
        validators=[MinValueValidator(1), MaxValueValidator(22)],
    )
    class Meta:
        verbose_name = "Декабрь"
        verbose_name_plural = "Декабрь"

    def __str__(self):
        return self.title
    
class BreakdownByYear(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название", help_text="1-2, 2-3, 3-4, 5, 6-7, 7-8, 8-9")
    description = RichTextField(verbose_name="Описание", help_text="Описание года/годов")
    
    class Meta:
        verbose_name = "Разбор по годам"
        verbose_name_plural = "Разбор по годам"

    def __str__(self):
        return self.title
