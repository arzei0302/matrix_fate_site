from rest_framework import serializers
from ..models import ChildCategory, QualitiesRevealedAgeOf20, ThirdTalentRevealedAge40

class QualitiesRevealedAgeOf20Serializer(serializers.ModelSerializer):
    class Meta:
        model = QualitiesRevealedAgeOf20
        fields = ["order_id", "title", "description"]

class ThirdTalentRevealedAge40Serializer(serializers.ModelSerializer):
    class Meta:
        model = ThirdTalentRevealedAge40
        fields = ["order_id", "title", "description"]

class ChildCategoryPersonalQualitiesSerializer(serializers.ModelSerializer):
    qualities_revealed_age_of_20 = QualitiesRevealedAgeOf20Serializer(many=True)
    third_talent_revealed_age_40 = ThirdTalentRevealedAge40Serializer(many=True)

    class Meta:
        model = ChildCategory
        fields = ["id", "title", "description", "is_paid", "qualities_revealed_age_of_20", "third_talent_revealed_age_40"]
