from rest_framework import serializers
from ..models import CompatibilityCategory, CoupleRelations1, CoupleRelations2, WhatRelationshipProblemsCanArise

class CoupleRelations1Serializer(serializers.ModelSerializer):
    class Meta:
        model = CoupleRelations1
        fields = ["order_id", "title", "description"]

class CoupleRelations2Serializer(serializers.ModelSerializer):
    class Meta:
        model = CoupleRelations2
        fields = ["order_id", "title", "description"]

class WhatRelationshipProblemsCanAriseSerializer(serializers.ModelSerializer):
    class Meta:
        model = WhatRelationshipProblemsCanArise
        fields = ["order_id", "title", "description"]

class CompatibilityCategoryCoupleRelationsSerializer(serializers.ModelSerializer):
    couple_relations_d2 = CoupleRelations1Serializer(many=True)
    couple_relations_k = CoupleRelations2Serializer(many=True)
    what_relationship_problems_can_arise_j = WhatRelationshipProblemsCanAriseSerializer(many=True)

    class Meta:
        model = CompatibilityCategory
        fields = [
            "id", "title", "description", "is_paid", 
            "couple_relations_d2", "couple_relations_k", "what_relationship_problems_can_arise_j"
        ]
