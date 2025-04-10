from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND
from django.shortcuts import get_object_or_404
from drf_spectacular.utils import extend_schema, OpenApiParameter

from common.permissions import IsActivePaidUser

from ..models import ChildCategory, ChildDestinyArcana1, ChildDestinyArcana2, ChildDestinyArcana3
from ..serializers.tasks_child_destiny_serializers import (
    ChildCategoryDestinySerializer,
    ChildDestinyArcana1Serializer,
    ChildDestinyArcana2Serializer,
    ChildDestinyArcana3Serializer,
)

@extend_schema(tags=["Child Matrix"])
class ChildCategoryWithDestinyAPIView(APIView):
    """
    Эндпоинт для получения категории (id=6 или title=Предназначение ребенка) + связанные арканы по order_id.
    """
    permission_classes = [IsActivePaidUser]
    serializer_class = ChildCategoryDestinySerializer

    @extend_schema(
        parameters=[
            OpenApiParameter(name="arcana_r", description="Аркан (r)", required=False, type=int),
            OpenApiParameter(name="arcana_s", description="Аркан (s)", required=False, type=int),
            OpenApiParameter(name="arcana_y", description="Аркан (y)", required=False, type=int),
        ]
    )
    def get(self, request, category_id_or_title):

        if category_id_or_title.isdigit():
            category = get_object_or_404(ChildCategory, id=int(category_id_or_title))
        else:
            category = get_object_or_404(ChildCategory, title__iexact=category_id_or_title)

        arcana_r_order = request.query_params.get("arcana_r")
        arcana_s_order = request.query_params.get("arcana_s")
        arcana_y_order = request.query_params.get("arcana_y")

        response_data = {
            "id": category.id,
            "title": category.title,
            "description": category.description,
            "is_paid": category.is_paid,
        }

        if arcana_r_order:
            try:
                arcana_r = ChildDestinyArcana1.objects.get(category=category, order_id=arcana_r_order)
                response_data["arcana_r"] = ChildDestinyArcana1Serializer(arcana_r).data
            except ChildDestinyArcana1.DoesNotExist:
                return Response(
                    {"error": f"Аркан с order_id={arcana_r_order} в ChildDestinyArcana1 не найден"},
                    status=HTTP_404_NOT_FOUND,
                )

        if arcana_s_order:
            try:
                arcana_s = ChildDestinyArcana2.objects.get(category=category, order_id=arcana_s_order)
                response_data["arcana_s"] = ChildDestinyArcana2Serializer(arcana_s).data
            except ChildDestinyArcana2.DoesNotExist:
                return Response(
                    {"error": f"Аркан с order_id={arcana_s_order} в ChildDestinyArcana2 не найден"},
                    status=HTTP_404_NOT_FOUND,
                )

        if arcana_y_order:
            try:
                arcana_y = ChildDestinyArcana3.objects.get(category=category, order_id=arcana_y_order)
                response_data["arcana_y"] = ChildDestinyArcana3Serializer(arcana_y).data
            except ChildDestinyArcana3.DoesNotExist:
                return Response(
                    {"error": f"Аркан с order_id={arcana_y_order} в ChildDestinyArcana3 не найден"},
                    status=HTTP_404_NOT_FOUND,
                )

        if not arcana_r_order and not arcana_s_order and not arcana_y_order:
            return Response(
                {"error": "Необходимо передать хотя бы один order_id аркана (arcana_r, arcana_s, arcana_y)"},
                status=HTTP_400_BAD_REQUEST,
            )

        return Response({"category": response_data})
