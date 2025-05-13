from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND
from django.shortcuts import get_object_or_404
from drf_spectacular.utils import extend_schema, OpenApiParameter

from ..models import Category, SoulComfortPoint
from ..serializers.soul_comfort_point_serializers import (
    CategorySoulComfortSerializer,
    SoulComfortPointSerializer,
)
from matrix_fate.common.mixins import PaidCategoryAccessMixin


@extend_schema(tags=["Matrix_Fate"])
class CategoryWithSoulComfortAPIView(APIView, PaidCategoryAccessMixin):
    """Получает категорию(id=7) или title(Точка душевного комфорта) и таланты по переданным `order_id`."""

    serializer_class = CategorySoulComfortSerializer

    @extend_schema(
        parameters=[
            OpenApiParameter(
                name="comfort",
                description="Точка душевного комфорта (e)",
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

        access_response = self.check_category_access(request, category)
        if access_response:
            return access_response

        comfort_order = request.query_params.get("comfort")

        if not comfort_order:
            return Response(
                {"error": "Необходимо передать число (comfort)"},
                status=HTTP_400_BAD_REQUEST,
            )

        try:
            soul_comfort_point = SoulComfortPoint.objects.get(
                category=category, order_id=comfort_order
            )
        except SoulComfortPoint.DoesNotExist:
            return Response(
                {
                    "error": f"Точка душевного комфорта с order_id={comfort_order} не найдена"
                },
                status=HTTP_404_NOT_FOUND,
            )

        return Response(
            {
                "category": {
                    "id": category.id,
                    "title": category.title,
                    "description": category.description,
                    "is_paid": category.is_paid,
                    "soul_comfort_point": SoulComfortPointSerializer(
                        soul_comfort_point
                    ).data,
                }
            }
        )
