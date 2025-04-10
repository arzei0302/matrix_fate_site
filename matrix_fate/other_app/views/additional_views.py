from rest_framework.response import Response
from rest_framework.views import APIView
from drf_spectacular.utils import extend_schema, OpenApiExample
import random
from other_app.serializers.additional_serializers import FutureCardSerializer, PastCardSerializer, PresentCardSerializer, TarotCardSerializer, ArcanaCluesSerializer
from ..models import FutureCard, PastCard, PresentCard, ArcanaClues


@extend_schema(
    tags=['Additional Calc'],
    responses={200: TarotCardSerializer(many=True)},
    examples=[
        OpenApiExample(
            name="Три карты",
            description="Про прошлое, настоящее и будущее",
            value={"past": "The Magician", "present": "The Lovers", "future": "The Tower"}
        )
    ]
)
class RandomTarotReadingView(APIView):
    """ПОДСКАЗКИ АРКАНОВ Про прошлое, настоящее и будущее """
    serializer_class = TarotCardSerializer
    def get(self, request):
        past_card = random.choice(PastCard.objects.all())
        present_card = random.choice(PresentCard.objects.all())
        future_card = random.choice(FutureCard.objects.all())

        result = [
            {'position': 'past', 'card': PastCardSerializer(past_card).data},
            {'position': 'present', 'card': PresentCardSerializer(present_card).data},
            {'position': 'future', 'card': FutureCardSerializer(future_card).data},
        ]

        serializer = self.serializer_class(result, many=True)
        return Response(serializer.data)


@extend_schema(
    tags=['Additional Calc'],
    responses={200: ArcanaCluesSerializer(many=True)},
    examples=[
        OpenApiExample(
            name="Три карты",
            description="Мысленно задайте вопрос и получите ответ ",
            value={"past": "The Magician", "present": "The Lovers", "future": "The Tower"}
        )
    ]
)
class RandomArcanaCluesView(APIView):
    """ПОДСКАЗКИ АРКАНОВ Мысленно задайте вопрос и получите ответ """
    serializer_class = ArcanaCluesSerializer

    def get(self, request):
        arcana_clues = random.choice(ArcanaClues.objects.all())
        serializer = self.serializer_class(arcana_clues)
        return Response(serializer.data)
