# Generated by Django 4.2.20 on 2025-04-03 06:04

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("prognosis_app", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="BreakdownByYear",
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
                        help_text="1-2, 2-3, 3-4, 5, 6-7, 7-8, 8-9",
                        max_length=255,
                        verbose_name="Название",
                    ),
                ),
                (
                    "description",
                    ckeditor.fields.RichTextField(
                        help_text="Описание года/годов", verbose_name="Описание"
                    ),
                ),
            ],
            options={
                "verbose_name": "Разбор по годам",
                "verbose_name_plural": "Разбор по годам",
            },
        ),
    ]
