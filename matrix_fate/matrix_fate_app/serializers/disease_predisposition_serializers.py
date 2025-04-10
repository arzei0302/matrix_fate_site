from rest_framework import serializers
from ..models import (
    Category,
    PaternalDiseases,
    MaternalDiseases,
    HealthArcane1,
    HealthArcane2,
    HealthArcane3,
)


class PaternalDiseasesSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaternalDiseases
        fields = ["order_id", "title", "description"]


class MaternalDiseasesSerializer(serializers.ModelSerializer):
    class Meta:
        model = MaternalDiseases
        fields = ["order_id", "title", "description"]


class HealthArcane1Serializer(serializers.ModelSerializer):
    class Meta:
        model = HealthArcane1
        fields = ["order_id", "title", "description"]


class HealthArcane2Serializer(serializers.ModelSerializer):
    class Meta:
        model = HealthArcane2
        fields = ["order_id", "title", "description"]


class HealthArcane3Serializer(serializers.ModelSerializer):
    class Meta:
        model = HealthArcane3
        fields = ["order_id", "title", "description"]


class CategoryWithDiseasePredispositionSerializer(serializers.ModelSerializer):
    paternal_diseases = PaternalDiseasesSerializer(many=True)
    maternal_diseases = MaternalDiseasesSerializer(many=True)
    health_arcane1 = HealthArcane1Serializer(many=True)
    health_arcane2 = HealthArcane2Serializer(many=True)
    health_arcane3 = HealthArcane3Serializer(many=True)

    class Meta:
        model = Category
        fields = [
            "id",
            "title",
            "description",
            "is_paid",
            "paternal_diseases",
            "maternal_diseases",
            "health_arcane1",
            "health_arcane2",
            "health_arcane3",
        ]
