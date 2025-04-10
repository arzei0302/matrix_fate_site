from rest_framework import serializers
from ..models import Category, PersonalPowerPoint


class PersonalPowerPointSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonalPowerPoint
        fields = ["order_id", "title", "description"]


class CategoryWithPersonalPowerSerializer(serializers.ModelSerializer):
    personal_power_points = PersonalPowerPointSerializer(many=True)

    class Meta:
        model = Category
        fields = ["id", "title", "description", "is_paid", "personal_power_points"]
