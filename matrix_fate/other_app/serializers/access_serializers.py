from rest_framework import serializers

from ..models import AccessMatrixModel


class AccessMatrixSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccessMatrixModel
        fields = ['id', 'name', 'description', 'is_active', 'order']
