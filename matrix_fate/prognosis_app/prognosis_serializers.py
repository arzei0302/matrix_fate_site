from rest_framework import serializers
from .models import (
    GeneralPrognosis, January, February, March, April, May, June, July,
    August, September, October, November, December
)


class BasePrognosisSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ["id", "title", "description", "order_id"]


class GeneralPrognosisSerializer(BasePrognosisSerializer):
    class Meta(BasePrognosisSerializer.Meta):
        model = GeneralPrognosis


class JanuarySerializer(BasePrognosisSerializer):
    class Meta(BasePrognosisSerializer.Meta):
        model = January


class FebruarySerializer(BasePrognosisSerializer):
    class Meta(BasePrognosisSerializer.Meta):
        model = February


class MarchSerializer(BasePrognosisSerializer):
    class Meta(BasePrognosisSerializer.Meta):
        model = March


class AprilSerializer(BasePrognosisSerializer):
    class Meta(BasePrognosisSerializer.Meta):
        model = April


class MaySerializer(BasePrognosisSerializer):
    class Meta(BasePrognosisSerializer.Meta):
        model = May


class JuneSerializer(BasePrognosisSerializer):
    class Meta(BasePrognosisSerializer.Meta):
        model = June


class JulySerializer(BasePrognosisSerializer):
    class Meta(BasePrognosisSerializer.Meta):
        model = July


class AugustSerializer(BasePrognosisSerializer):
    class Meta(BasePrognosisSerializer.Meta):
        model = August


class SeptemberSerializer(BasePrognosisSerializer):
    class Meta(BasePrognosisSerializer.Meta):
        model = September


class OctoberSerializer(BasePrognosisSerializer):
    class Meta(BasePrognosisSerializer.Meta):
        model = October


class NovemberSerializer(BasePrognosisSerializer):
    class Meta(BasePrognosisSerializer.Meta):
        model = November


class DecemberSerializer(BasePrognosisSerializer):
    class Meta(BasePrognosisSerializer.Meta):
        model = December
