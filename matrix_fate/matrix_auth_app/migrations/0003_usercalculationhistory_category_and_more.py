# Generated by Django 4.2.20 on 2025-04-16 04:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('matrix_auth_app', '0002_usercalculationhistory'),
    ]

    operations = [
        migrations.AddField(
            model_name='usercalculationhistory',
            name='category',
            field=models.CharField(choices=[('matrix_fate', 'Калькулятор Матрица судьбы'), ('finance', 'Калькулятор Финансы'), ('compatibility', 'Калькулятор Совместимость'), ('child', 'Калькулятор Детская матрица')], default='matrix_fate', max_length=20, verbose_name='Раздел'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='access_expiration',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Дата окончания доступа'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='access_level',
            field=models.CharField(choices=[('level1', 'Бесплатный'), ('level2', 'Разовый'), ('level3', 'Месячный'), ('level4', 'Годовой')], default='level1', max_length=20, verbose_name='Уровень доступа'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='avatars/', verbose_name='Аватар'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='full_name',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Полное имя'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='phone',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Телефон'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
        migrations.AlterField(
            model_name='usercalculationhistory',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='usercalculationhistory',
            name='input_data',
            field=models.JSONField(verbose_name='Входные данные'),
        ),
        migrations.AlterField(
            model_name='usercalculationhistory',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='calculations', to='matrix_auth_app.profile', verbose_name='Профиль'),
        ),
        migrations.AlterField(
            model_name='usercalculationhistory',
            name='result_data',
            field=models.JSONField(verbose_name='Результат расчета'),
        ),
    ]
