from rest_framework import serializers
from ..models import (
    Category,
    PersonalPurpose1,
    PersonalPurpose2,
    PersonalPurpose3,
    SocialPurpose1,
    SocialPurpose2,
    SocialPurpose3,
    SpiritualPurpose,
)


class PersonalPurpose1Serializer(serializers.ModelSerializer):
    class Meta:
        model = PersonalPurpose1
        fields = ["order_id", "title", "description"]


class PersonalPurpose2Serializer(serializers.ModelSerializer):
    class Meta:
        model = PersonalPurpose2
        fields = ["order_id", "title", "description"]


class PersonalPurpose3Serializer(serializers.ModelSerializer):
    class Meta:
        model = PersonalPurpose3
        fields = ["order_id", "title", "description"]


class SocialPurpose1Serializer(serializers.ModelSerializer):
    class Meta:
        model = SocialPurpose1
        fields = ["order_id", "title", "description"]


class SocialPurpose2Serializer(serializers.ModelSerializer):
    class Meta:
        model = SocialPurpose2
        fields = ["order_id", "title", "description"]


class SocialPurpose3Serializer(serializers.ModelSerializer):
    class Meta:
        model = SocialPurpose3
        fields = ["order_id", "title", "description"]


class SpiritualPurposeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpiritualPurpose
        fields = ["order_id", "title", "description"]


class CategoryWithSoulMissionSerializer(serializers.ModelSerializer):
    personal_purpose_1 = PersonalPurpose1Serializer(many=True)
    personal_purpose_2 = PersonalPurpose2Serializer(many=True)
    personal_purpose_3 = PersonalPurpose3Serializer(many=True)
    social_purpose_1 = SocialPurpose1Serializer(many=True)
    social_purpose_2 = SocialPurpose2Serializer(many=True)
    social_purpose_3 = SocialPurpose3Serializer(many=True)
    spiritual_purpose = SpiritualPurposeSerializer(many=True)

    class Meta:
        model = Category
        fields = [
            "id",
            "title",
            "description",
            "is_paid",
            "personal_purpose_1",
            "personal_purpose_2",
            "personal_purpose_3",
            "social_purpose_1",
            "social_purpose_2",
            "social_purpose_3",
            "spiritual_purpose",
        ]
