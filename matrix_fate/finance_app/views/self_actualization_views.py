from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND
from django.shortcuts import get_object_or_404
from drf_spectacular.utils import extend_schema, OpenApiParameter

from matrix_fate.finance_app.serializers.self_actualization_serializers import (
    YourOpportunitySerializer,
    FinanceCategorySelfActualizationSerializer,
)

from ..models import FinanceCategory, YourOpportunity


@extend_schema(tags=["Finance Matrix"])
class FinanceCategoryWithOpportunityAPIView(APIView):
    """Получает категорию по `id(2)` или `title(Самореализация)` и связанные таблицы по переданному order_id."""

    serializer_class = FinanceCategorySelfActualizationSerializer

    @extend_schema(
        parameters=[
            OpenApiParameter(
                name="opportunity",
                description="Ваша возможность (a2)",
                required=True,
                type=int,
            ),
        ]
    )
    def get(self, request, category_id_or_title):

        if category_id_or_title.isdigit():
            category = get_object_or_404(FinanceCategory, id=int(category_id_or_title))
        else:
            category = get_object_or_404(
                FinanceCategory, title__iexact=category_id_or_title
            )

        opportunity_order = request.query_params.get("opportunity")

        if not opportunity_order:
            return Response(
                {"error": "Необходимо передать order_id для возможности"},
                status=HTTP_400_BAD_REQUEST,
            )

        try:
            opportunity = YourOpportunity.objects.get(
                category=category, order_id=opportunity_order
            )
        except YourOpportunity.DoesNotExist:
            return Response(
                {"error": f"Возможность с order_id={opportunity_order} не найдена"},
                status=HTTP_404_NOT_FOUND,
            )

        return Response(
            {
                "category": {
                    "id": category.id,
                    "title": category.title,
                    "description": category.description,
                    "is_paid": category.is_paid,
                    "opportunity": YourOpportunitySerializer(opportunity).data,
                }
            }
        )
