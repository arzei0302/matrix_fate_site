from rest_framework import serializers
from ..models import ChildCategory, ChildPointOfComfort

class ChildPointOfComfortSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChildPointOfComfort
        fields = ["order_id", "title", "description"]

class ChildCategoryPointOfComfortSerializer(serializers.ModelSerializer):
    child_point_of_comfort = ChildPointOfComfortSerializer(many=True)

    class Meta:
        model = ChildCategory
        fields = ["id", "title", "description", "is_paid", "child_point_of_comfort"]
