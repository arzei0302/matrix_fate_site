from rest_framework import serializers
from ..models import (
    Category,
    BirthTalent,
    YouthTalent,
    MatureTalent,
)


class BirthTalentSerializer(serializers.ModelSerializer):
    class Meta:
        model = BirthTalent
        fields = ["order_id", "title", "description"]


class YouthTalentSerializer(serializers.ModelSerializer):
    class Meta:
        model = YouthTalent
        fields = ["order_id", "title", "description"]


class MatureTalentSerializer(serializers.ModelSerializer):
    class Meta:
        model = MatureTalent
        fields = ["order_id", "title", "description"]


class CategorySerializer(serializers.ModelSerializer):
    birth_talents = BirthTalentSerializer(many=True)
    youth_talents = YouthTalentSerializer(many=True)
    mature_talents = MatureTalentSerializer(many=True)

    class Meta:
        model = Category
        fields = [
            "id",
            "title",
            "description",
            "is_paid",
            "birth_talents",
            "youth_talents",
            "mature_talents",
        ]
