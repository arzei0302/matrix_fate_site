from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND
from django.shortcuts import get_object_or_404
from drf_spectacular.utils import extend_schema, OpenApiParameter

from matrix_fate.common.permissions import IsActivePaidUser

from ..models import Category, PersonalPowerPoint
from ..serializers.personal_power_point_serializers import (
    CategoryWithPersonalPowerSerializer,
    PersonalPowerPointSerializer,
)


@extend_schema(tags=["Matrix_Fate"])
class CategoryWithPersonalPowerAPIView(APIView):
    """Получает категорию по `id(10)` или `title(Точка личной силы)` и точку личной силы по переданному номеру (order_id)."""

    permission_classes = [IsActivePaidUser]
    serializer_class = CategoryWithPersonalPowerSerializer

    @extend_schema(
        parameters=[
            OpenApiParameter(
                name="order",
                description="№ аркана точки личной силы (e)",
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
                {"error": "Необходимо передать order (№ аркана точки личной силы)"},
                status=HTTP_400_BAD_REQUEST,
            )

        try:
            personal_power_point = PersonalPowerPoint.objects.get(
                category=category, order_id=order_id
            )
        except PersonalPowerPoint.DoesNotExist:
            return Response(
                {"error": f"Точка личной силы с order_id={order_id} не найдена"},
                status=HTTP_404_NOT_FOUND,
            )

        return Response(
            {
                "category": {
                    "id": category.id,
                    "title": category.title,
                    "description": category.description,
                    "is_paid": category.is_paid,
                    "personal_power_point": PersonalPowerPointSerializer(
                        personal_power_point
                    ).data,
                }
            }
        )
