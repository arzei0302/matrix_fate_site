from rest_framework import serializers
from ..models import Category, SpiritualTask1, SpiritualTask2, SpiritualTask3


class SpiritualTask1Serializer(serializers.ModelSerializer):
    class Meta:
        model = SpiritualTask1
        fields = ["order_id", "title", "description"]


class SpiritualTask2Serializer(serializers.ModelSerializer):
    class Meta:
        model = SpiritualTask2
        fields = ["order_id", "title", "description"]


class SpiritualTask3Serializer(serializers.ModelSerializer):
    class Meta:
        model = SpiritualTask3
        fields = ["order_id", "title", "description"]


class CategoryWithSpiritualKarmaSerializer(serializers.ModelSerializer):
    spiritual_task_1 = SpiritualTask1Serializer(many=True)
    spiritual_task_2 = SpiritualTask2Serializer(many=True)
    spiritual_task_3 = SpiritualTask3Serializer(many=True)

    class Meta:
        model = Category
        fields = [
            "id",
            "title",
            "description",
            "is_paid",
            "spiritual_task_1",
            "spiritual_task_2",
            "spiritual_task_3",
        ]
