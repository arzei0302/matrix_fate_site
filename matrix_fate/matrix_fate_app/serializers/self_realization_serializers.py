from rest_framework import serializers
from ..models import Category, SelfRealization


class SelfRealizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = SelfRealization
        fields = ["order_id", "title", "description"]


class CategorySelfRealizationSerializer(serializers.ModelSerializer):
    self_realizations = SelfRealizationSerializer(many=True)

    class Meta:
        model = Category
        fields = ["id", "title", "description", "is_paid", "self_realizations"]
