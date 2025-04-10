from rest_framework import serializers
from ..models import (
    FinanceCategory,
    YourGreatestTalentBirth,
    QualitiesRevealedAge20,
    QualitiesDevelopAge40,
)


class YourGreatestTalentBirthSerializer(serializers.ModelSerializer):
    class Meta:
        model = YourGreatestTalentBirth
        fields = ["order_id", "title", "description"]


class QualitiesRevealedAge20Serializer(serializers.ModelSerializer):
    class Meta:
        model = QualitiesRevealedAge20
        fields = ["order_id", "title", "description"]


class QualitiesDevelopAge40Serializer(serializers.ModelSerializer):
    class Meta:
        model = QualitiesDevelopAge40
        fields = ["order_id", "title", "description"]


class FinanceCategoryTalentsSerializer(serializers.ModelSerializer):
    your_greatest_talent_birth = YourGreatestTalentBirthSerializer(many=True)
    qualities_revealed_age_20 = QualitiesRevealedAge20Serializer(many=True)
    qualities_develop_age_40 = QualitiesDevelopAge40Serializer(many=True)

    class Meta:
        model = FinanceCategory
        fields = [
            "id",
            "title",
            "description",
            "is_paid",
            "your_greatest_talent_birth",
            "qualities_revealed_age_20",
            "qualities_develop_age_40",
        ]
