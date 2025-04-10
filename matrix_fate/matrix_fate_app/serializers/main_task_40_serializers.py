from rest_framework import serializers
from ..models import Category, MainTask40, TaskBefore40, TaskAfter40


class MainTask40Serializer(serializers.ModelSerializer):
    class Meta:
        model = MainTask40
        fields = ["order_id", "title", "description"]


class TaskBefore40Serializer(serializers.ModelSerializer):
    class Meta:
        model = TaskBefore40
        fields = ["order_id", "title", "description"]


class TaskAfter40Serializer(serializers.ModelSerializer):
    class Meta:
        model = TaskAfter40
        fields = ["order_id", "title", "description"]


class CategoryMainTask40Serializer(serializers.ModelSerializer):
    main_tasks_40 = MainTask40Serializer(many=True)
    tasks_before_40 = TaskBefore40Serializer(many=True)
    tasks_after_40 = TaskAfter40Serializer(many=True)

    class Meta:
        model = Category
        fields = [
            "id",
            "title",
            "description",
            "is_paid",
            "main_tasks_40",
            "tasks_before_40",
            "tasks_after_40",
        ]
