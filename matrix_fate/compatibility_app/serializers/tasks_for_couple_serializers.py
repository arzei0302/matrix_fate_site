from rest_framework import serializers
from ..models import CompatibilityCategory, TasksForCoupleArcana1, TasksForCoupleArcana2, TasksForCoupleArcana3

class TasksForCoupleArcana1Serializer(serializers.ModelSerializer):
    class Meta:
        model = TasksForCoupleArcana1
        fields = ["order_id", "title", "description"]

class TasksForCoupleArcana2Serializer(serializers.ModelSerializer):
    class Meta:
        model = TasksForCoupleArcana2
        fields = ["order_id", "title", "description"]

class TasksForCoupleArcana3Serializer(serializers.ModelSerializer):
    class Meta:
        model = TasksForCoupleArcana3
        fields = ["order_id", "title", "description"]

class CompatibilityCategoryTasksForCoupleSerializer(serializers.ModelSerializer):
    tasks_for_couple_w = TasksForCoupleArcana1Serializer(many=True)
    tasks_for_couple_d = TasksForCoupleArcana2Serializer(many=True)
    tasks_for_couple_y = TasksForCoupleArcana3Serializer(many=True)

    class Meta:
        model = CompatibilityCategory
        fields = [
            "id", "title", "description", "is_paid", 
            "tasks_for_couple_w", "tasks_for_couple_d", "tasks_for_couple_y"
        ]
