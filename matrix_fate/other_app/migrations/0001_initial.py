# Generated by Django 4.2.20 on 2025-03-16 17:39

import ckeditor.fields
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="AccessMatrixModel",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255, verbose_name="Название")),
                ("description", ckeditor.fields.RichTextField(verbose_name="Описание")),
                (
                    "is_active",
                    models.BooleanField(default=True, verbose_name="Активен"),
                ),
                (
                    "order",
                    models.PositiveSmallIntegerField(
                        blank=True, null=True, verbose_name="Порядковый номер"
                    ),
                ),
            ],
            options={
                "verbose_name": "Таблица доступов",
                "verbose_name_plural": "Таблицы доступов",
            },
        ),
        migrations.CreateModel(
            name="ArcanaClues",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=255, verbose_name="Название")),
                ("description", ckeditor.fields.RichTextField(verbose_name="Описание")),
                (
                    "image",
                    models.ImageField(
                        upload_to="arcana_clues/", verbose_name="Изображение"
                    ),
                ),
            ],
            options={
                "verbose_name": "Подсказка арканов",
                "verbose_name_plural": "Подсказки арканов",
            },
        ),
        migrations.CreateModel(
            name="FinancialAndAntiCodeCalculation",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=255, verbose_name="Название")),
                ("description", ckeditor.fields.RichTextField(verbose_name="Описание")),
                (
                    "order_id",
                    models.PositiveSmallIntegerField(
                        validators=[
                            django.core.validators.MinValueValidator(1),
                            django.core.validators.MaxValueValidator(22),
                        ],
                        verbose_name="№ аркана",
                    ),
                ),
                (
                    "image",
                    models.ImageField(
                        upload_to="financial_and_anti_code_calculations/",
                        verbose_name="Изображение",
                    ),
                ),
            ],
            options={
                "verbose_name": "Калькуляция финансов и антикодов",
                "verbose_name_plural": "Калькуляции финансов и антикодов",
            },
        ),
        migrations.CreateModel(
            name="FutureCard",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "title",
                    models.CharField(max_length=255, verbose_name="Название (Будущее)"),
                ),
                ("description", ckeditor.fields.RichTextField(verbose_name="Описание")),
                (
                    "image",
                    models.ImageField(
                        upload_to="future_cards/", verbose_name="Изображение"
                    ),
                ),
            ],
            options={
                "verbose_name": "Карта Будущее",
                "verbose_name_plural": "Карты Будущее",
            },
        ),
        migrations.CreateModel(
            name="LandingPage",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=255, verbose_name="Название")),
                (
                    "sub_title",
                    models.CharField(max_length=255, verbose_name="Подзаголовок"),
                ),
                ("description", ckeditor.fields.RichTextField(verbose_name="Описание")),
                (
                    "sub_description",
                    ckeditor.fields.RichTextField(verbose_name="Подописание"),
                ),
                ("order_id", models.PositiveSmallIntegerField()),
                ("reference1", models.CharField(max_length=255, verbose_name="Ссылка")),
                ("reference2", models.CharField(max_length=255, verbose_name="Ссылка")),
                (
                    "image1",
                    models.ImageField(
                        upload_to="landing_page/", verbose_name="Изображение1"
                    ),
                ),
                (
                    "image2",
                    models.ImageField(
                        upload_to="landing_page/", verbose_name="Изображение2"
                    ),
                ),
                (
                    "image3",
                    models.ImageField(
                        upload_to="landing_page/", verbose_name="Изображение3"
                    ),
                ),
                (
                    "image4",
                    models.ImageField(
                        upload_to="landing_page/", verbose_name="Изображение4"
                    ),
                ),
                (
                    "image5",
                    models.ImageField(
                        upload_to="landing_page/", verbose_name="Изображение5"
                    ),
                ),
            ],
            options={
                "verbose_name": "Баннер/Лендинг",
                "verbose_name_plural": "Баннеры/Лендинги",
            },
        ),
        migrations.CreateModel(
            name="MessageSupport",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=255, verbose_name="Название")),
                ("description", ckeditor.fields.RichTextField(verbose_name="Описание")),
                ("reference", models.CharField(max_length=255, verbose_name="Ссылка")),
            ],
            options={
                "verbose_name": "Написать в поддержку",
                "verbose_name_plural": "Написать в поддержку",
            },
        ),
        migrations.CreateModel(
            name="PastCard",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "title",
                    models.CharField(max_length=255, verbose_name="Название (Прошлое)"),
                ),
                ("description", ckeditor.fields.RichTextField(verbose_name="Описание")),
                (
                    "image",
                    models.ImageField(
                        upload_to="past_cards/", verbose_name="Изображение"
                    ),
                ),
            ],
            options={
                "verbose_name": "Карта Прошлое",
                "verbose_name_plural": "Карты Прошлое",
            },
        ),
        migrations.CreateModel(
            name="PresentCard",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "title",
                    models.CharField(
                        max_length=255, verbose_name="Название (Настоящее)"
                    ),
                ),
                ("description", ckeditor.fields.RichTextField(verbose_name="Описание")),
                (
                    "image",
                    models.ImageField(
                        upload_to="present_cards/", verbose_name="Изображение"
                    ),
                ),
            ],
            options={
                "verbose_name": "Карта Настоящее",
                "verbose_name_plural": "Карты Настоящее",
            },
        ),
        migrations.CreateModel(
            name="PrivacyPolicy",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=255, verbose_name="Название")),
                ("description", ckeditor.fields.RichTextField(verbose_name="Описание")),
            ],
            options={
                "verbose_name": "Политика конфиденциальности",
                "verbose_name_plural": "Политика конфиденциальности",
            },
        ),
        migrations.CreateModel(
            name="PublicOfferAgreement",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=255, verbose_name="Название")),
                ("description", ckeditor.fields.RichTextField(verbose_name="Описание")),
            ],
            options={
                "verbose_name": "Публичное предложение",
                "verbose_name_plural": "Публичное предложение",
            },
        ),
    ]
