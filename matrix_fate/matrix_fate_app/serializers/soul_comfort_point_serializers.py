from rest_framework import serializers
from ..models import Category, SoulComfortPoint


class SoulComfortPointSerializer(serializers.ModelSerializer):
    class Meta:
        model = SoulComfortPoint
        fields = ["order_id", "title", "description"]


class CategorySoulComfortSerializer(serializers.ModelSerializer):
    soul_comfort_points = SoulComfortPointSerializer(many=True)

    class Meta:
        model = Category
        fields = ["id", "title", "description", "is_paid", "soul_comfort_points"]
