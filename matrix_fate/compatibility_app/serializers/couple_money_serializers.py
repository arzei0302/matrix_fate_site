from rest_framework import serializers
from ..models import CompatibilityCategory, WhatGivesTribute, WhatTasksUnlockMoneyChannels, WhatBlocksMonetaryEnergy

class WhatGivesTributeSerializer(serializers.ModelSerializer):
    class Meta:
        model = WhatGivesTribute
        fields = ["order_id", "title", "description"]

class WhatTasksUnlockMoneyChannelsSerializer(serializers.ModelSerializer):
    class Meta:
        model = WhatTasksUnlockMoneyChannels
        fields = ["order_id", "title", "description"]

class WhatBlocksMonetaryEnergySerializer(serializers.ModelSerializer):
    class Meta:
        model = WhatBlocksMonetaryEnergy
        fields = ["order_id", "title", "description"]

class CompatibilityCategoryCoupleMoneySerializer(serializers.ModelSerializer):
    what_gives_tribute_k = WhatGivesTributeSerializer(many=True)
    what_tasks_unlock_money_channels_j = WhatTasksUnlockMoneyChannelsSerializer(many=True)
    what_blocks_monetary_energy_i1 = WhatBlocksMonetaryEnergySerializer(many=True)

    class Meta:
        model = CompatibilityCategory
        fields = [
            "id", "title", "description", "is_paid", 
            "what_gives_tribute_k", "what_tasks_unlock_money_channels_j", "what_blocks_monetary_energy_i1"
        ]
