from rest_framework import serializers
from .models import BreakdownByYear

class BreakdownByYearSerializer(serializers.ModelSerializer):
    class Meta:
        model = BreakdownByYear
        fields = ['id', 'title', 'description']