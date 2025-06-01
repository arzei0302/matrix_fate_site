from rest_framework import serializers
from ..models import (
    Category,
    SuitableProfessions,
    MoneySources,
    MoneyGrowthTasks1,
    MoneyGrowthTasks2,
    MoneyBlocks,
    MoneyUnblock,
)


class SuitableProfessionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SuitableProfessions
        fields = ["order_id", "title", "description"]


class MoneySourcesSerializer(serializers.ModelSerializer):
    class Meta:
        model = MoneySources
        fields = ["order_id", "title", "description"]


# class MoneyGrowthTasks1Serializer(serializers.ModelSerializer):
#     class Meta:
#         model = MoneyGrowthTasks1
#         fields = ["order_id", "title", "description"]


# class MoneyGrowthTasks2Serializer(serializers.ModelSerializer):
#     class Meta:
#         model = MoneyGrowthTasks2
#         fields = ["order_id", "title", "description"]


class MoneyBlocksSerializer(serializers.ModelSerializer):
    class Meta:
        model = MoneyBlocks
        fields = ["order_id", "title", "description"]


# class MoneyUnblockSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = MoneyUnblock
#         fields = ["order_id", "title", "description"]


class CategoryWithMatrixMoneySerializer(serializers.ModelSerializer):
    suitable_professions = SuitableProfessionsSerializer(many=True)
    money_sources = MoneySourcesSerializer(many=True)
    # money_growth_tasks1 = MoneyGrowthTasks1Serializer(many=True)
    # money_growth_tasks2 = MoneyGrowthTasks2Serializer(many=True)
    money_blocks = MoneyBlocksSerializer(many=True)
    # money_unblock = MoneyUnblockSerializer(many=True)

    class Meta:
        model = Category
        fields = [
            "id",
            "title",
            "description",
            "is_paid",
            "suitable_professions",
            "money_sources",
            # "money_growth_tasks1",
            # "money_growth_tasks2",
            "money_blocks",
            # "money_unblock",
        ]
