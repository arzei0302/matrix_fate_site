from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiResponse
from datetime import datetime

from common.permissions import IsActivePaidUser

from .models import (
    GeneralPrognosis, January, February, March, April, May, June, July,
    August, September, October, November, December
)
from .prognosis_serializers import (
    GeneralPrognosisSerializer, JanuarySerializer, FebruarySerializer, MarchSerializer,
    AprilSerializer, MaySerializer, JuneSerializer, JulySerializer, AugustSerializer,
    SeptemberSerializer, OctoberSerializer, NovemberSerializer, DecemberSerializer
)


def reduce_to_22(number: int) -> int:
    """Суммирует цифры числа, если оно больше 22."""
    while number > 22:
        number = sum(int(d) for d in str(number))
    return number


@extend_schema(
    tags=["Matrix Prognosis"],
    parameters=[
        OpenApiParameter(
            name="birth_date",
            description="Дата рождения в формате ДД.ММ.ГГГГ",
            required=True,
            type=str,
        ),
    ],
    responses={
        200: OpenApiResponse(description="Возвращает прогнозы по дате рождения из всех источников"),
        400: OpenApiResponse(response={"error": "birth_date is required"}, description="Дата не передана"),
        404: OpenApiResponse(response={"message": "No records found"}, description="Нет данных"),
    },
)
class PrognosisByBirthDateAPIView(APIView):
    """
    API для получения прогнозов на основе даты рождения.
    """
    permission_classes = [IsActivePaidUser]

    def get(self, request):
        birth_date_str = request.query_params.get("birth_date")

        if not birth_date_str:
            return Response(
                {"error": "birth_date is required"},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            birth_date = datetime.strptime(birth_date_str, "%d.%m.%Y").date()
        except ValueError:
            return Response(
                {"error": "birth_date должен быть в формате ДД.ММ.ГГГГ"},
                status=status.HTTP_400_BAD_REQUEST
            )

        date_number = int(birth_date.strftime("%Y%m%d"))
        order_id = reduce_to_22(date_number)

        models = [
            (GeneralPrognosis, GeneralPrognosisSerializer),
            (January, JanuarySerializer),
            (February, FebruarySerializer),
            (March, MarchSerializer),
            (April, AprilSerializer),
            (May, MaySerializer),
            (June, JuneSerializer),
            (July, JulySerializer),
            (August, AugustSerializer),
            (September, SeptemberSerializer),
            (October, OctoberSerializer),
            (November, NovemberSerializer),
            (December, DecemberSerializer),
        ]

        result = {}

        for model, serializer in models:
            instances = model.objects.filter(order_id=order_id)
            if instances.exists():
                result[model._meta.verbose_name_plural] = serializer(instances, many=True).data

        if not result:
            return Response(
                {"message": f"No records found for order_id {order_id}"},
                status=status.HTTP_404_NOT_FOUND
            )

        return Response(result, status=status.HTTP_200_OK)
