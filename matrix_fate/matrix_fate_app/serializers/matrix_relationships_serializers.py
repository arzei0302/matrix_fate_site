from rest_framework import serializers
from ..models import (
    Category,
    PartnerTasks,
    SuitablePartner,
    MeetingPlace,
    RelationshipProblems,
)


class PartnerTasksSerializer(serializers.ModelSerializer):
    class Meta:
        model = PartnerTasks
        fields = ["order_id", "title", "description"]


class SuitablePartnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = SuitablePartner
        fields = ["order_id", "title", "description"]


# class MeetingPlaceSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = MeetingPlace
#         fields = ["order_id", "title", "description"]


class RelationshipProblemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = RelationshipProblems
        fields = ["order_id", "title", "description"]


class CategoryWithMatrixRelationshipsSerializer(serializers.ModelSerializer):
    partner_tasks = PartnerTasksSerializer(many=True)
    suitable_partners = SuitablePartnerSerializer(many=True)
    # meeting_places = MeetingPlaceSerializer(many=True)
    relationship_problems = RelationshipProblemsSerializer(many=True)

    class Meta:
        model = Category
        fields = [
            "id",
            "title",
            "description",
            "is_paid",
            "partner_tasks",
            "suitable_partners",
            # "meeting_places",
            "relationship_problems",
        ]
