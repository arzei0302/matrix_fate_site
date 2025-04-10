from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND
from django.shortcuts import get_object_or_404
from drf_spectacular.utils import extend_schema, OpenApiParameter

from ..models import Category, AncestralPower
from ..serializers.ancestral_power_serializers import (
    CategoryWithAncestralPowerSerializer,
    AncestralPowerSerializer,
)


@extend_schema(tags=["Matrix_Fate"])
class CategoryWithAncestralPowerAPIView(APIView):
    """Получает категорию по `id(11)` или `title(Сила рода)` и силу рода по переданному номеру (order_id)."""

    serializer_class = CategoryWithAncestralPowerSerializer

    @extend_schema(
        parameters=[
            OpenApiParameter(
                name="order",
                description="№ аркана силы рода (e1)",
                required=True,
                type=int,
            ),
        ]
    )
    def get(self, request, category_id_or_title):
        if category_id_or_title.isdigit():
            category = get_object_or_404(Category, id=int(category_id_or_title))
        else:
            category = get_object_or_404(Category, title__iexact=category_id_or_title)

        order_id = request.query_params.get("order")

        if not order_id:
            return Response(
                {"error": "Необходимо передать order (№ аркана силы рода)"},
                status=HTTP_400_BAD_REQUEST,
            )

        try:
            ancestral_power = AncestralPower.objects.get(
                category=category, order_id=order_id
            )
        except AncestralPower.DoesNotExist:
            return Response(
                {"error": f"Сила рода с order_id={order_id} не найдена"},
                status=HTTP_404_NOT_FOUND,
            )

        return Response(
            {
                "category": {
                    "id": category.id,
                    "title": category.title,
                    "description": category.description,
                    "is_paid": category.is_paid,
                    "ancestral_power": AncestralPowerSerializer(ancestral_power).data,
                }
            }
        )
