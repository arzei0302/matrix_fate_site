from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from rest_framework import serializers


class OrderMarkerMixin(models.Model):
    order_id = models.PositiveSmallIntegerField(
        verbose_name="№ аркана",
        validators=[MinValueValidator(1), MaxValueValidator(22)],
        null=True,
        blank=True,
    )
    marker = models.CharField(
        max_length=10,
        null=True,
        blank=True,
        verbose_name="Маркер",
        help_text="Идентификатор ключа на схеме матрицы, например 'a'"
    )

    class Meta:
        abstract = True


class ErrorSerializer(serializers.Serializer):
    error = serializers.CharField()

