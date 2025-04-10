# Generated by Django 4.2.20 on 2025-03-17 18:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("matrix_auth_app", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="UserCalculationHistory",
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
                ("input_data", models.JSONField()),
                ("result_data", models.JSONField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "profile",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="calculations",
                        to="matrix_auth_app.profile",
                    ),
                ),
            ],
            options={
                "verbose_name": "История расчетов",
                "verbose_name_plural": "История расчетов",
            },
        ),
    ]
