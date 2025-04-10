from rest_framework import serializers
from ..models import (
    ChildCategory,
    ChildDestinyArcana1,
    ChildDestinyArcana2,
    ChildDestinyArcana3,
)

class ChildDestinyArcana1Serializer(serializers.ModelSerializer):
    class Meta:
        model = ChildDestinyArcana1
        fields = ["order_id", "title", "description"]

class ChildDestinyArcana2Serializer(serializers.ModelSerializer):
    class Meta:
        model = ChildDestinyArcana2
        fields = ["order_id", "title", "description"]

class ChildDestinyArcana3Serializer(serializers.ModelSerializer):
    class Meta:
        model = ChildDestinyArcana3
        fields = ["order_id", "title", "description"]

class ChildCategoryDestinySerializer(serializers.ModelSerializer):
    child_destiny_arcana1 = ChildDestinyArcana1Serializer(many=True)
    child_destiny_arcana2 = ChildDestinyArcana2Serializer(many=True)
    child_destiny_arcana3 = ChildDestinyArcana3Serializer(many=True)

    class Meta:
        model = ChildCategory
        fields = [
            "id", "title", "description", "is_paid",
            "child_destiny_arcana1", "child_destiny_arcana2", "child_destiny_arcana3"
        ]
