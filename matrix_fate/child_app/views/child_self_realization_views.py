from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND
from django.shortcuts import get_object_or_404
from drf_spectacular.utils import extend_schema, OpenApiParameter

from matrix_fate.common.permissions import IsActivePaidUser

from ..models import ChildCategory, ChildOpportunity
from ..serializers.child_self_realization_serializers import (
    ChildCategorySelfRealizationSerializer,
    ChildOpportunitySerializer,
)

@extend_schema(tags=["Child Matrix"])
class ChildCategoryWithSelfRealizationAPIView(APIView):
    """
    Эндпоинт для получения категории (id=3 или title=Самореализация ребенка) + связанный аркан по order_id.
    """
    permission_classes = [IsActivePaidUser]
    serializer_class = ChildCategorySelfRealizationSerializer

    @extend_schema(
        parameters=[
            OpenApiParameter(
                name="arcana_a2", description="Аркан (a2)", required=True, type=int
            ),
        ]
    )
    def get(self, request, category_id_or_title):

        if category_id_or_title.isdigit():
            category = get_object_or_404(
                ChildCategory, id=int(category_id_or_title)
            )
        else:
            category = get_object_or_404(
                ChildCategory, title__iexact=category_id_or_title
            )

        arcana_order = request.query_params.get("arcana_a2")

        if not arcana_order:
            return Response(
                {"error": "Необходимо передать order_id аркана (arcana_a2)"},
                status=HTTP_400_BAD_REQUEST,
            )

        try:
            arcana = ChildOpportunity.objects.get(category=category, order_id=arcana_order)
        except ChildOpportunity.DoesNotExist:
            return Response(
                {"error": f"Аркан с order_id={arcana_order} в ChildOpportunity не найден"},
                status=HTTP_404_NOT_FOUND,
            )

        return Response(
            {
                "category": {
                    "id": category.id,
                    "title": category.title,
                    "description": category.description,
                    "is_paid": category.is_paid,
                    "arcana": ChildOpportunitySerializer(arcana).data,
                }
            }
        )
