from rest_framework import serializers
from ..models import Category, SoulMainTask, PastLifeExperience, PastLifeLesson


class SoulMainTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = SoulMainTask
        fields = ["order_id", "title", "description"]


class PastLifeExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = PastLifeExperience
        fields = ["order_id", "title", "description"]


class PastLifeLessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = PastLifeLesson
        fields = ["order_id", "title", "description"]


class CategoryPastLifeTaskSerializer(serializers.ModelSerializer):
    soul_main_tasks = SoulMainTaskSerializer(many=True)
    past_life_experiences = PastLifeExperienceSerializer(many=True)
    past_life_lessons = PastLifeLessonSerializer(many=True)

    class Meta:
        model = Category
        fields = [
            "id",
            "title",
            "description",
            "is_paid",
            "soul_main_tasks",
            "past_life_experiences",
            "past_life_lessons",
        ]
