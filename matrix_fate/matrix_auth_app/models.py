import random
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
#

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Email is required')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"


class EmailVerificationCode(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    code = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.code:
            self.code = str(random.randint(100000, 999999))
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Код верификации"
        verbose_name_plural = "Коды верификации"


ACCESS_LEVEL_CHOICES = [
    ('level1', 'Бесплатный'),
    ('level2', 'Разовый'),
    ('level3', 'Месячный'),
    ('level4', 'Годовой'),
]

ACCESS_EXPIRATION_DAYS = {
    'level1': None,
    'level2': 1,
    'level3': 30,
    'level4': 365,
}


class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, verbose_name="Пользователь", related_name='profile')
    full_name = models.CharField(max_length=255, blank=True, verbose_name="Полное имя", null=True)
    phone = models.CharField(max_length=20, blank=True, verbose_name="Телефон", null=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True, verbose_name="Аватар", null=True)
    access_level = models.CharField(max_length=20, verbose_name="Уровень доступа", choices=ACCESS_LEVEL_CHOICES, default='level1')
    access_expiration = models.DateTimeField(blank=True, verbose_name="Дата окончания доступа", null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    def __str__(self):
        return f'Профиль {self.user.email} ({self.get_access_level_display()})'

    class Meta:
        verbose_name = "Профиль"
        verbose_name_plural = "Профили"


class UserCalculationHistory(models.Model):

    # CATEGORY_CHOICES = [
    #     ('matrix_fate', 'Калькулятор Матрица судьбы'),
    #     ('finance', 'Калькулятор Финансы'),
    #     ('compatibility', 'Калькулятор Совместимость'),
    #     ('child', 'Калькулятор Детская матрица'),
    # ]
    CATEGORY_CHOICES = [
        ('matrix_fate', 'Kohtalomatriisi laskin'),
        ('finance', 'Talouslaskin'),
        ('compatibility', 'Yhteensopivuuslaskin'),
        ('child', 'Lasten matriisi laskin'),
    ]


    profile = models.ForeignKey('Profile', on_delete=models.CASCADE, related_name='calculations', verbose_name="Профиль")
    input_data = models.JSONField(verbose_name="Входные данные")
    result_data = models.JSONField(verbose_name="Результат расчета")
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, verbose_name="Раздел", default='matrix_fate')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    def __str__(self):
        return f'Расчет {self.profile.user.email} ({self.created_at})'

    class Meta:
        verbose_name = "История расчетов"
        verbose_name_plural = "История расчетов"

