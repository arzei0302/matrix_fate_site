from rest_framework import serializers
from ..models import ChildCategory, ChildBusinessCard

class ChildBusinessCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChildBusinessCard
        fields = ["order_id", "title", "description"]

class ChildCategoryGreatestTalentSerializer(serializers.ModelSerializer):
    child_business_card = ChildBusinessCardSerializer(many=True)

    class Meta:
        model = ChildCategory
        fields = ["id", "title", "description", "is_paid", "child_business_card"]
