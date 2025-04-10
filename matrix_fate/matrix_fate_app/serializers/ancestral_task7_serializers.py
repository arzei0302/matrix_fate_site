from rest_framework import serializers
from ..models import (
    Category,
    AncestralTaskFatherMale,
    AncestralTaskMotherMale,
    AncestralTaskFatherFemale,
    AncestralTaskMotherFemale,
)


class AncestralTaskFatherMaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = AncestralTaskFatherMale
        fields = ["order_id", "title", "description"]


class AncestralTaskMotherMaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = AncestralTaskMotherMale
        fields = ["order_id", "title", "description"]


class AncestralTaskFatherFemaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = AncestralTaskFatherFemale
        fields = ["order_id", "title", "description"]


class AncestralTaskMotherFemaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = AncestralTaskMotherFemale
        fields = ["order_id", "title", "description"]


class CategoryWithAncestralTask7Serializer(serializers.ModelSerializer):
    ancestral_tasks_father_male = AncestralTaskFatherMaleSerializer(many=True)
    ancestral_tasks_mother_male = AncestralTaskMotherMaleSerializer(many=True)
    ancestral_tasks_father_female = AncestralTaskFatherFemaleSerializer(many=True)
    ancestral_tasks_mother_female = AncestralTaskMotherFemaleSerializer(many=True)

    class Meta:
        model = Category
        fields = [
            "id",
            "title",
            "description",
            "is_paid",
            "ancestral_tasks_father_male",
            "ancestral_tasks_mother_male",
            "ancestral_tasks_father_female",
            "ancestral_tasks_mother_female",
        ]
