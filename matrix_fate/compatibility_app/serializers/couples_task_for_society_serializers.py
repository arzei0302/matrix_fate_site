from rest_framework import serializers
from ..models import CompatibilityCategory, CouplesTaskForSociety

class CouplesTaskForSocietySerializer(serializers.ModelSerializer):
    class Meta:
        model = CouplesTaskForSociety
        fields = ["order_id", "title", "description"]

class CompatibilityCategoryCouplesTaskSerializer(serializers.ModelSerializer):
    couples_task_for_society_v = CouplesTaskForSocietySerializer(many=True)

    class Meta:
        model = CompatibilityCategory
        fields = [
            "id", "title", "description", "is_paid", 
            "couples_task_for_society_v"
        ]
