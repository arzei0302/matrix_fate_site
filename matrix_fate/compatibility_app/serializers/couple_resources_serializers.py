from rest_framework import serializers
from ..models import CompatibilityCategory, CoupleResourcesArcana1, CoupleResourcesArcana2

class CoupleResourcesArcana1Serializer(serializers.ModelSerializer):
    class Meta:
        model = CoupleResourcesArcana1
        fields = ["order_id", "title", "description"]

class CoupleResourcesArcana2Serializer(serializers.ModelSerializer):
    class Meta:
        model = CoupleResourcesArcana2
        fields = ["order_id", "title", "description"]

class CompatibilityCategoryCoupleResourcesSerializer(serializers.ModelSerializer):
    couple_resources_b = CoupleResourcesArcana1Serializer(many=True)
    couple_resources_c = CoupleResourcesArcana2Serializer(many=True)

    class Meta:
        model = CompatibilityCategory
        fields = [
            "id", "title", "description", "is_paid", 
            "couple_resources_b", "couple_resources_c"
        ]
