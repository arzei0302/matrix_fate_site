from rest_framework.views import APIView
from rest_framework import serializers

from rest_framework.response import Response
from rest_framework import status
from drf_spectacular.utils import extend_schema, OpenApiExample, OpenApiParameter
import random

class YesNoMaybeAnswerSerializer(serializers.Serializer):
    number = serializers.IntegerField()
    answer = serializers.CharField()

def yes_no_maybe(number: int) -> str:
    """
    Принимает трёхзначное число и возвращает один из ответов:
    "да", "нет", "скорее да, чем нет".
    """
    if not (100 <= number <= 999):
        raise ValueError("Ожидается трёхзначное число (от 100 до 999)")
    return random.choice(["да", "нет", "скорее да, чем нет"])

@extend_schema(
    tags=["Additional Calc"],
    parameters=[
        OpenApiParameter(
            name="number",
            description="Трёхзначное число, пришедшее в голову",
            required=True,
            type=int,
            location=OpenApiParameter.QUERY
        )
    ],
    responses={200: YesNoMaybeAnswerSerializer},
    examples=[
        OpenApiExample(
            name="Да / Нет",
            description="Мысленно задайте вопрос и введите трёхзначное число",
            value={"number": 345, "answer": "скорее да, чем нет"}
        )
    ]
)
class YesNoMaybeAnswerView(APIView):
    """ДА / НЕТ / СКОРЕЕ ДА — мысленно задайте вопрос и введите трёхзначное число"""

    def get(self, request):
        number_str = request.query_params.get("number")
        if not number_str:
            return Response({"error": "Параметр 'number' обязателен"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            number = int(number_str)
        except ValueError:
            return Response({"error": "'number' должен быть числом"}, status=status.HTTP_400_BAD_REQUEST)

        if number < 100 or number > 999:
            return Response({"error": "'number' должен быть трёхзначным числом (от 100 до 999)"}, status=status.HTTP_400_BAD_REQUEST)

        answer = yes_no_maybe(number)
        return Response({"number": number, "answer": answer})
