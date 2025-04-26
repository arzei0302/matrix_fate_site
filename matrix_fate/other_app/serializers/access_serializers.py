from rest_framework import serializers

from ..models import AccessMatrixModel


class AccessMatrixSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccessMatrixModel
        fields = ['id', 'name', 'description', 'price', 'is_active', 'order']
