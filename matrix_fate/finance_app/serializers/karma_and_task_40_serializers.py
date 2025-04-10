from rest_framework import serializers
from ..models import (
    FinanceCategory,
    TheMainTask40Years,
    WhatBeforeYouTurn40Years,
    WhatAfterYouTurn40Years,
)

class TheMainTask40YearsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TheMainTask40Years
        fields = ["order_id", "title", "description"]

class WhatBeforeYouTurn40YearsSerializer(serializers.ModelSerializer):
    class Meta:
        model = WhatBeforeYouTurn40Years
        fields = ["order_id", "title", "description"]

class WhatAfterYouTurn40YearsSerializer(serializers.ModelSerializer):
    class Meta:
        model = WhatAfterYouTurn40Years
        fields = ["order_id", "title", "description"]

class FinanceCategorySerializer(serializers.ModelSerializer):
    the_main_task_40_years = TheMainTask40YearsSerializer(many=True)
    what_before_you_turn_40_years = WhatBeforeYouTurn40YearsSerializer(many=True)
    what_after_you_turn_40_years = WhatAfterYouTurn40YearsSerializer(many=True)

    class Meta:
        model = FinanceCategory
        fields = [
            "id", "title", "description", "is_paid",
            "the_main_task_40_years",
            "what_before_you_turn_40_years",
            "what_after_you_turn_40_years"
        ]
