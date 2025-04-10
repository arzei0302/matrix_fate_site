from rest_framework import serializers
from ..models import (
    FinanceCategory,
    TaskPersonalArcana1,
    TaskPersonalArcana2,
    TaskPersonalArcana3,
)


class TaskPersonalArcana1Serializer(serializers.ModelSerializer):
    class Meta:
        model = TaskPersonalArcana1
        fields = ["order_id", "title", "description"]


class TaskPersonalArcana2Serializer(serializers.ModelSerializer):
    class Meta:
        model = TaskPersonalArcana2
        fields = ["order_id", "title", "description"]


class TaskPersonalArcana3Serializer(serializers.ModelSerializer):
    class Meta:
        model = TaskPersonalArcana3
        fields = ["order_id", "title", "description"]


class FinanceCategoryDestinationSocietySerializer(serializers.ModelSerializer):
    task_personal_arcana_1 = TaskPersonalArcana1Serializer(many=True)
    task_personal_arcana_2 = TaskPersonalArcana2Serializer(many=True)
    task_personal_arcana_3 = TaskPersonalArcana3Serializer(many=True)

    class Meta:
        model = FinanceCategory
        fields = [
            "id",
            "title",
            "description",
            "is_paid",
            "task_personal_arcana_1",
            "task_personal_arcana_2",
            "task_personal_arcana_3",
        ]
