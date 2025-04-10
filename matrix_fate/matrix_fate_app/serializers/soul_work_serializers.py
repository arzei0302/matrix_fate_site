from rest_framework import serializers
from ..models import Category, InnateTalent, QualitiesRevealed, QualitiesDeveloped


class InnateTalentSerializer(serializers.ModelSerializer):
    class Meta:
        model = InnateTalent
        fields = ["order_id", "title", "description"]


class QualitiesRevealedSerializer(serializers.ModelSerializer):
    class Meta:
        model = QualitiesRevealed
        fields = ["order_id", "title", "description"]


class QualitiesDevelopedSerializer(serializers.ModelSerializer):
    class Meta:
        model = QualitiesDeveloped
        fields = ["order_id", "title", "description"]


class CategorySoulWorkSerializer(serializers.ModelSerializer):
    innate_talents = InnateTalentSerializer(many=True)
    qualities_revealed = QualitiesRevealedSerializer(many=True)
    qualities_developed = QualitiesDevelopedSerializer(many=True)

    class Meta:
        model = Category
        fields = [
            "id",
            "title",
            "description",
            "is_paid",
            "innate_talents",
            "qualities_revealed",
            "qualities_developed",
        ]
