from rest_framework import serializers
from ..models import FinanceCategory, YourOpportunity


class YourOpportunitySerializer(serializers.ModelSerializer):
    class Meta:
        model = YourOpportunity
        fields = ["order_id", "title", "description"]


class FinanceCategorySelfActualizationSerializer(serializers.ModelSerializer):
    your_opportunity = YourOpportunitySerializer(many=True)

    class Meta:
        model = FinanceCategory
        fields = ["id", "title", "description", "is_paid", "your_opportunity"]
