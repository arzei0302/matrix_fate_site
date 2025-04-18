# Generated by Django 4.2.20 on 2025-03-15 15:21

import ckeditor.fields
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="FinanceCategory",
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
                        help_text="Название категории",
                        max_length=255,
                        verbose_name="Название категории",
                    ),
                ),
                (
                    "description",
                    ckeditor.fields.RichTextField(
                        help_text="Описание категории",
                        verbose_name="Описание категории",
                    ),
                ),
                (
                    "is_paid",
                    models.BooleanField(
                        default=False, verbose_name="Платная категория"
                    ),
                ),
            ],
            options={
                "verbose_name": "Категория",
                "verbose_name_plural": "Категории",
            },
        ),
        migrations.CreateModel(
            name="YourOpportunity",
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
                        help_text="Ваша возможность (a2)",
                        max_length=255,
                        verbose_name="Название",
                    ),
                ),
                (
                    "description",
                    ckeditor.fields.RichTextField(
                        help_text="Ваша возможность (a2)", verbose_name="Описание"
                    ),
                ),
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
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="your_opportunity",
                        to="finance_app.financecategory",
                    ),
                ),
            ],
            options={
                "verbose_name": "Ваша возможность",
                "verbose_name_plural": "Ваша возможность",
                "unique_together": {("category", "order_id")},
            },
        ),
        migrations.CreateModel(
            name="YourGreatestTalentBirth",
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
                        help_text="Ваш главный талант от рождения (a)",
                        max_length=255,
                        verbose_name="Название",
                    ),
                ),
                (
                    "description",
                    ckeditor.fields.RichTextField(
                        help_text="Ваш главный талант от рождения (a)",
                        verbose_name="Описание",
                    ),
                ),
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
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="your_greatest_talent_birth",
                        to="finance_app.financecategory",
                    ),
                ),
            ],
            options={
                "verbose_name": "Ваш главный талант от рождения",
                "verbose_name_plural": "Ваш главный талант от рождения",
                "unique_together": {("category", "order_id")},
            },
        ),
        migrations.CreateModel(
            name="WhatOpensYourMoneyChannel",
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
                        help_text="Что открывает ваш денежный канал (i1)",
                        max_length=255,
                        verbose_name="Название",
                    ),
                ),
                (
                    "description",
                    ckeditor.fields.RichTextField(
                        help_text="Что открывает ваш денежный канал (i1)",
                        verbose_name="Описание",
                    ),
                ),
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
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="what_opens_your_money_channel",
                        to="finance_app.financecategory",
                    ),
                ),
            ],
            options={
                "verbose_name": "Что открывает ваш денежный канал",
                "verbose_name_plural": "Что открывает ваш денежный канал",
                "unique_together": {("category", "order_id")},
            },
        ),
        migrations.CreateModel(
            name="WhatGivesYouMoney",
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
                        help_text="Что дает деньги (j)",
                        max_length=255,
                        verbose_name="Название",
                    ),
                ),
                (
                    "description",
                    ckeditor.fields.RichTextField(
                        help_text="Что дает деньги (j)", verbose_name="Описание"
                    ),
                ),
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
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="what_gives_you_money",
                        to="finance_app.financecategory",
                    ),
                ),
            ],
            options={
                "verbose_name": "Что дает деньги",
                "verbose_name_plural": "Что дает деньги",
                "unique_together": {("category", "order_id")},
            },
        ),
        migrations.CreateModel(
            name="WhatBlocksMoneyEnergy",
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
                        help_text="Что блокирует денежную энергию: (k)",
                        max_length=255,
                        verbose_name="Название",
                    ),
                ),
                (
                    "description",
                    ckeditor.fields.RichTextField(
                        help_text="Что блокирует денежную энергию: (k)",
                        verbose_name="Описание",
                    ),
                ),
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
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="what_blocks_money_energy",
                        to="finance_app.financecategory",
                    ),
                ),
            ],
            options={
                "verbose_name": "Что блокирует денежную энергию",
                "verbose_name_plural": "Что блокирует денежную энергию",
                "unique_together": {("category", "order_id")},
            },
        ),
        migrations.CreateModel(
            name="TasksOpenMoneyChannel2",
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
                        help_text="Какие нужно проработать задачи, чтобы раскрыть денежный канал: (c2)",
                        max_length=255,
                        verbose_name="Название",
                    ),
                ),
                (
                    "description",
                    ckeditor.fields.RichTextField(
                        help_text="Какие нужно проработать задачи, чтобы раскрыть денежный канал: (c2)",
                        verbose_name="Описание",
                    ),
                ),
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
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="tasks_open_money_channel2",
                        to="finance_app.financecategory",
                    ),
                ),
            ],
            options={
                "verbose_name": "Задачаи открытия денежного канала2",
                "verbose_name_plural": "Задачи открытия денежного канала2",
                "unique_together": {("category", "order_id")},
            },
        ),
        migrations.CreateModel(
            name="TasksOpenMoneyChannel1",
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
                        help_text="Какие нужно проработать задачи, чтобы раскрыть денежный канал: (i1)",
                        max_length=255,
                        verbose_name="Название",
                    ),
                ),
                (
                    "description",
                    ckeditor.fields.RichTextField(
                        help_text="Какие нужно проработать задачи, чтобы раскрыть денежный канал: (i1)",
                        verbose_name="Описание",
                    ),
                ),
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
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="tasks_open_money_channel1",
                        to="finance_app.financecategory",
                    ),
                ),
            ],
            options={
                "verbose_name": "Задачаи открытия денежного канала1",
                "verbose_name_plural": "Задачи открытия денежного канала1",
                "unique_together": {("category", "order_id")},
            },
        ),
        migrations.CreateModel(
            name="TaskPersonalArcana3",
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
                        help_text="Задача для персонального аркана1 (y)",
                        max_length=255,
                        verbose_name="Название",
                    ),
                ),
                (
                    "description",
                    ckeditor.fields.RichTextField(
                        help_text="Описание задачи для персонального аркана1 (y)",
                        verbose_name="Описание",
                    ),
                ),
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
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="task_personal_arcana_3",
                        to="finance_app.financecategory",
                    ),
                ),
            ],
            options={
                "verbose_name": "Персональная задача 3",
                "verbose_name_plural": "Персональные задачи 3",
                "unique_together": {("category", "order_id")},
            },
        ),
        migrations.CreateModel(
            name="TaskPersonalArcana2",
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
                        help_text="Задача для персонального аркана2 (s)",
                        max_length=255,
                        verbose_name="Название",
                    ),
                ),
                (
                    "description",
                    ckeditor.fields.RichTextField(
                        help_text="Описание задачи для персонального аркана2 (s)",
                        verbose_name="Описание",
                    ),
                ),
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
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="task_personal_arcana_2",
                        to="finance_app.financecategory",
                    ),
                ),
            ],
            options={
                "verbose_name": "Персональная задача 2",
                "verbose_name_plural": "Персональные задачи 2",
                "unique_together": {("category", "order_id")},
            },
        ),
        migrations.CreateModel(
            name="TaskPersonalArcana1",
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
                        help_text="Задача для персонального аркана1 (r)",
                        max_length=255,
                        verbose_name="Название",
                    ),
                ),
                (
                    "description",
                    ckeditor.fields.RichTextField(
                        help_text="Описание задачи для персонального аркана1 (r)",
                        verbose_name="Описание",
                    ),
                ),
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
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="task_personal_arcana_1",
                        to="finance_app.financecategory",
                    ),
                ),
            ],
            options={
                "verbose_name": "Персональная задача 1",
                "verbose_name_plural": "Персональные задачи 1",
                "unique_together": {("category", "order_id")},
            },
        ),
        migrations.CreateModel(
            name="QualitiesRevealedAge20",
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
                        help_text="Качества которые раскрываются к 20 годам (b)",
                        max_length=255,
                        verbose_name="Название",
                    ),
                ),
                (
                    "description",
                    ckeditor.fields.RichTextField(
                        help_text="Качества которые раскрываются к 20 годам (b)",
                        verbose_name="Описание",
                    ),
                ),
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
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="qualities_revealed_age_20",
                        to="finance_app.financecategory",
                    ),
                ),
            ],
            options={
                "verbose_name": "Качества которые раскрываются к 20 годам",
                "verbose_name_plural": "Качества которые раскрываются к 20 годам",
                "unique_together": {("category", "order_id")},
            },
        ),
        migrations.CreateModel(
            name="QualitiesDevelopAge40",
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
                        help_text="Качества которые мы должны в себе наработать до 40 лет (c)",
                        max_length=255,
                        verbose_name="Название",
                    ),
                ),
                (
                    "description",
                    ckeditor.fields.RichTextField(
                        help_text="Качества которые мы должны в себе наработать до 40 лет (c)",
                        verbose_name="Описание",
                    ),
                ),
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
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="qualities_develop_age_40",
                        to="finance_app.financecategory",
                    ),
                ),
            ],
            options={
                "verbose_name": "Качества которые мы должны в себе наработать до 40 лет",
                "verbose_name_plural": "Качества которые мы должны в себе наработать до 40 лет",
                "unique_together": {("category", "order_id")},
            },
        ),
        migrations.CreateModel(
            name="AreasOfRealization",
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
                        help_text="Сферы реализации (c2)",
                        max_length=255,
                        verbose_name="Название",
                    ),
                ),
                (
                    "description",
                    ckeditor.fields.RichTextField(
                        help_text="Сферы реализации (c2)", verbose_name="Описание"
                    ),
                ),
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
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="areas_of_realization",
                        to="finance_app.financecategory",
                    ),
                ),
            ],
            options={
                "verbose_name": "Область реализации",
                "verbose_name_plural": "Сферы реализации",
                "unique_together": {("category", "order_id")},
            },
        ),
    ]
