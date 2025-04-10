from rest_framework import serializers
from ..models import (
    FinanceCategory,
    TasksOpenMoneyChannel1,
    TasksOpenMoneyChannel2,
    WhatBlocksMoneyEnergy,
)


class TasksOpenMoneyChannel1Serializer(serializers.ModelSerializer):
    class Meta:
        model = TasksOpenMoneyChannel1
        fields = ["order_id", "title", "description"]


class TasksOpenMoneyChannel2Serializer(serializers.ModelSerializer):
    class Meta:
        model = TasksOpenMoneyChannel2
        fields = ["order_id", "title", "description"]


class WhatBlocksMoneyEnergySerializer(serializers.ModelSerializer):
    class Meta:
        model = WhatBlocksMoneyEnergy
        fields = ["order_id", "title", "description"]


class FinanceCategoryBlocksMoneySerializer(serializers.ModelSerializer):
    tasks_open_money_channel1 = TasksOpenMoneyChannel1Serializer(many=True)
    tasks_open_money_channel2 = TasksOpenMoneyChannel2Serializer(many=True)
    what_blocks_money_energy = WhatBlocksMoneyEnergySerializer(many=True)

    class Meta:
        model = FinanceCategory
        fields = [
            "id",
            "title",
            "description",
            "is_paid",
            "tasks_open_money_channel1",
            "tasks_open_money_channel2",
            "what_blocks_money_energy",
        ]
