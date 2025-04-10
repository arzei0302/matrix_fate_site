from rest_framework import serializers
from ..models import (
    ChildCategory,
    MainTaskSoul,
    SoulPastExperiencesWithPeople,
    LessonsFromPastLife,
)

class MainTaskSoulSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainTaskSoul
        fields = ["order_id", "title", "description"]

class SoulPastExperiencesWithPeopleSerializer(serializers.ModelSerializer):
    class Meta:
        model = SoulPastExperiencesWithPeople
        fields = ["order_id", "title", "description"]

class LessonsFromPastLifeSerializer(serializers.ModelSerializer):
    class Meta:
        model = LessonsFromPastLife
        fields = ["order_id", "title", "description"]

class ChildCategoryFromPastLivesSerializer(serializers.ModelSerializer):
    main_task_soul = MainTaskSoulSerializer(many=True)
    soul_past_experiences_with_people = SoulPastExperiencesWithPeopleSerializer(many=True)
    lessons_from_past_life = LessonsFromPastLifeSerializer(many=True)

    class Meta:
        model = ChildCategory
        fields = [
            "id", "title", "description", "is_paid",
            "main_task_soul", "soul_past_experiences_with_people", "lessons_from_past_life"
        ]
