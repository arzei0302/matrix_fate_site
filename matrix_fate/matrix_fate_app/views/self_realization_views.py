from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND
from django.shortcuts import get_object_or_404
from drf_spectacular.utils import extend_schema, OpenApiParameter

from ..models import Category, SelfRealization
from ..serializers.self_realization_serializers import (
    CategorySelfRealizationSerializer,
    SelfRealizationSerializer,
)
from matrix_fate.common.mixins import PaidCategoryAccessMixin


@extend_schema(tags=["Matrix_Fate"])
class CategoryWithSelfRealizationAPIView(APIView, PaidCategoryAccessMixin):
    """Получает категорию(id=8) или title(Самореализация) и таланты по переданным `order_id`."""

    serializer_class = CategorySelfRealizationSerializer

    @extend_schema(
        parameters=[
            OpenApiParameter(
                name="realization",
                description="Ваша возможность (a2)",
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

        realization_order = request.query_params.get("realization")

        if not realization_order:
            return Response(
                {"error": "Необходимо передать число (realization)"},
                status=HTTP_400_BAD_REQUEST,
            )

        try:
            self_realization = SelfRealization.objects.get(
                category=category, order_id=realization_order
            )
        except SelfRealization.DoesNotExist:
            return Response(
                {"error": f"Самореализация с order_id={realization_order} не найдена"},
                status=HTTP_404_NOT_FOUND,
            )

        return Response(
            {
                "category": {
                    "id": category.id,
                    "title": category.title,
                    "description": category.description,
                    "is_paid": category.is_paid,
                    "self_realization": SelfRealizationSerializer(
                        self_realization
                    ).data,
                }
            }
        )
