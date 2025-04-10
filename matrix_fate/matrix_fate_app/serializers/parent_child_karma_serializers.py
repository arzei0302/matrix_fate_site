from rest_framework import serializers
from ..models import Category, TeachParents, RelationshipMistakes, PersonalGrowth


class TeachParentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeachParents
        fields = ["order_id", "title", "description"]


class RelationshipMistakesSerializer(serializers.ModelSerializer):
    class Meta:
        model = RelationshipMistakes
        fields = ["order_id", "title", "description"]


class PersonalGrowthSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonalGrowth
        fields = ["order_id", "title", "description"]


class CategoryWithParentChildKarmaSerializer(serializers.ModelSerializer):
    teach_parents = TeachParentsSerializer(many=True)
    relationship_mistakes = RelationshipMistakesSerializer(many=True)
    personal_growth = PersonalGrowthSerializer(many=True)

    class Meta:
        model = Category
        fields = [
            "id",
            "title",
            "description",
            "is_paid",
            "teach_parents",
            "relationship_mistakes",
            "personal_growth",
        ]
