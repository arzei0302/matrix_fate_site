from rest_framework import serializers

from ..models import FutureCard, PastCard, PresentCard, ArcanaClues

class PastCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = PastCard
        fields = ['id', 'title', 'description', 'image']

class PresentCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = PresentCard
        fields = ['id', 'title', 'description', 'image']

class FutureCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = FutureCard
        fields = ['id', 'title', 'description', 'image']


class TarotCardSerializer(serializers.Serializer):
    position = serializers.ChoiceField(choices=['past', 'present', 'future'])
    card = serializers.DictField()


class ArcanaCluesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArcanaClues
        fields = ['id', 'title', 'description', 'image']