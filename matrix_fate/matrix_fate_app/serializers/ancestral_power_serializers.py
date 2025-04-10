from rest_framework import serializers
from ..models import Category, AncestralPower


class AncestralPowerSerializer(serializers.ModelSerializer):
    class Meta:
        model = AncestralPower
        fields = ["order_id", "title", "description"]


class CategoryWithAncestralPowerSerializer(serializers.ModelSerializer):
    ancestral_powers = AncestralPowerSerializer(many=True)

    class Meta:
        model = Category
        fields = ["id", "title", "description", "is_paid", "ancestral_powers"]
