from rest_framework import serializers
from ..models import ChildCategory, ChildOpportunity

class ChildOpportunitySerializer(serializers.ModelSerializer):
    class Meta:
        model = ChildOpportunity
        fields = ["order_id", "title", "description"]

class ChildCategorySelfRealizationSerializer(serializers.ModelSerializer):
    child_opportunity = ChildOpportunitySerializer(many=True)

    class Meta:
        model = ChildCategory
        fields = ["id", "title", "description", "is_paid", "child_opportunity"]
