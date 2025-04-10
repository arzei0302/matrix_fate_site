from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND
from django.shortcuts import get_object_or_404
from drf_spectacular.utils import extend_schema, OpenApiParameter

from ..models import ChildCategory, ChildPointOfComfort
from ..serializers.child_point_of_comfort_serializers import (
    ChildCategoryPointOfComfortSerializer,
    ChildPointOfComfortSerializer,
)

@extend_schema(tags=["Child Matrix"])
class ChildCategoryWithPointOfComfortAPIView(APIView):
    """
    Эндпоинт для получения категории (id=4 или title=Точка душевного комфорта ребенка) + связанный аркан по order_id.
    """

    serializer_class = ChildCategoryPointOfComfortSerializer

    @extend_schema(
        parameters=[
            OpenApiParameter(
                name="arcana_e", description="Аркан (e)", required=True, type=int
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

        arcana_order = request.query_params.get("arcana_e")

        if not arcana_order:
            return Response(
                {"error": "Необходимо передать order_id аркана (arcana_e)"},
                status=HTTP_400_BAD_REQUEST,
            )

        try:
            arcana = ChildPointOfComfort.objects.get(category=category, order_id=arcana_order)
        except ChildPointOfComfort.DoesNotExist:
            return Response(
                {"error": f"Аркан с order_id={arcana_order} в ChildPointOfComfort не найден"},
                status=HTTP_404_NOT_FOUND,
            )

        return Response(
            {
                "category": {
                    "id": category.id,
                    "title": category.title,
                    "description": category.description,
                    "is_paid": category.is_paid,
                    "arcana": ChildPointOfComfortSerializer(arcana).data,
                }
            }
        )
