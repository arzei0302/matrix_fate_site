from rest_framework import serializers
from ..models import CompatibilityCategory, WhyDidYouMeet

class WhyDidYouMeetSerializer(serializers.ModelSerializer):
    class Meta:
        model = WhyDidYouMeet
        fields = ["order_id", "title", "description"]

class CompatibilityCategorySerializer(serializers.ModelSerializer):
    why_did_you_meet = WhyDidYouMeetSerializer(many=True)

    class Meta:
        model = CompatibilityCategory
        fields = ["id", "title", "description", "is_paid", "why_did_you_meet"]
