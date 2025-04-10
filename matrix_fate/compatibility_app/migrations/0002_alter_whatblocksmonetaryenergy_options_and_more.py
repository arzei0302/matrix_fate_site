# Generated by Django 4.2.20 on 2025-03-16 18:22

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("compatibility_app", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="whatblocksmonetaryenergy",
            options={
                "verbose_name": "Что блокирует денежную энергию: (j)",
                "verbose_name_plural": "Что блокирует денежную энергию: (j)",
            },
        ),
        migrations.AlterModelOptions(
            name="whatgivestribute",
            options={
                "verbose_name": "Что дает деньги (c2)",
                "verbose_name_plural": "Что дает деньги (c2)",
            },
        ),
        migrations.AlterModelOptions(
            name="whattasksunlockmoneychannels",
            options={
                "verbose_name": "Какие нужно проработать задачи, чтобы раскрыть денежный канал: (l)",
                "verbose_name_plural": "Какие нужно проработать задачи, чтобы раскрыть денежный канал: (l)",
            },
        ),
        migrations.AlterField(
            model_name="whatblocksmonetaryenergy",
            name="category",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="what_blocks_monetary_energy_j",
                to="compatibility_app.compatibilitycategory",
            ),
        ),
        migrations.AlterField(
            model_name="whatblocksmonetaryenergy",
            name="description",
            field=ckeditor.fields.RichTextField(
                help_text="Что блокирует денежную энергию: (j)", verbose_name="Описание"
            ),
        ),
        migrations.AlterField(
            model_name="whatblocksmonetaryenergy",
            name="title",
            field=models.CharField(
                help_text="Что блокирует денежную энергию: (j)",
                max_length=255,
                verbose_name="Название",
            ),
        ),
        migrations.AlterField(
            model_name="whatgivestribute",
            name="category",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="what_gives_tribute_c2",
                to="compatibility_app.compatibilitycategory",
            ),
        ),
        migrations.AlterField(
            model_name="whatgivestribute",
            name="description",
            field=ckeditor.fields.RichTextField(
                help_text="Что дает деньги (c2)", verbose_name="Описание"
            ),
        ),
        migrations.AlterField(
            model_name="whatgivestribute",
            name="title",
            field=models.CharField(
                help_text="Что дает деньги (c2)",
                max_length=255,
                verbose_name="Название",
            ),
        ),
        migrations.AlterField(
            model_name="whattasksunlockmoneychannels",
            name="category",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="what_tasks_unlock_money_channels_l",
                to="compatibility_app.compatibilitycategory",
            ),
        ),
        migrations.AlterField(
            model_name="whattasksunlockmoneychannels",
            name="description",
            field=ckeditor.fields.RichTextField(
                help_text="Какие нужно проработать задачи, чтобы раскрыть денежный канал: (l)",
                verbose_name="Описание",
            ),
        ),
        migrations.AlterField(
            model_name="whattasksunlockmoneychannels",
            name="title",
            field=models.CharField(
                help_text="Какие нужно проработать задачи, чтобы раскрыть денежный канал: (l)",
                max_length=255,
                verbose_name="Название",
            ),
        ),
    ]
