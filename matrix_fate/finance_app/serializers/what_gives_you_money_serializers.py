from rest_framework import serializers
from ..models import (
    FinanceCategory,
    WhatGivesYouMoney,
    WhatOpensYourMoneyChannel,
    AreasOfRealization,
)


class WhatGivesYouMoneySerializer(serializers.ModelSerializer):
    class Meta:
        model = WhatGivesYouMoney
        fields = ["order_id", "title", "description"]


class WhatOpensYourMoneyChannelSerializer(serializers.ModelSerializer):
    class Meta:
        model = WhatOpensYourMoneyChannel
        fields = ["order_id", "title", "description"]


class AreasOfRealizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = AreasOfRealization
        fields = ["order_id", "title", "description"]


class FinanceCategoryWhatGivesYouMoneySerializer(serializers.ModelSerializer):
    what_gives_you_money = WhatGivesYouMoneySerializer(many=True)
    what_opens_your_money_channel = WhatOpensYourMoneyChannelSerializer(many=True)
    areas_of_realization = AreasOfRealizationSerializer(many=True)

    class Meta:
        model = FinanceCategory
        fields = [
            "id",
            "title",
            "description",
            "is_paid",
            "what_gives_you_money",
            "what_opens_your_money_channel",
            "areas_of_realization",
        ]
