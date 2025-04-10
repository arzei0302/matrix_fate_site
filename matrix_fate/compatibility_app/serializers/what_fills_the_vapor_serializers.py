from rest_framework import serializers
from ..models import CompatibilityCategory, WhatFillsTheVapor

class WhatFillsTheVaporSerializer(serializers.ModelSerializer):
    class Meta:
        model = WhatFillsTheVapor
        fields = ["order_id", "title", "description"]

class CompatibilityCategoryWhatFillsSerializer(serializers.ModelSerializer):
    what_fills_the_vapor_e = WhatFillsTheVaporSerializer(many=True)

    class Meta:
        model = CompatibilityCategory
        fields = [
            "id", "title", "description", "is_paid", 
            "what_fills_the_vapor_e"
        ]
