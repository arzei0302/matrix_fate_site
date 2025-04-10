from rest_framework import serializers
from other_app.models import FinancialAndAntiCodeCalculation


class FinancialAndAntiCodeCalculationSerializer(serializers.ModelSerializer):
    class Meta:
        model = FinancialAndAntiCodeCalculation
        fields = '__all__'
