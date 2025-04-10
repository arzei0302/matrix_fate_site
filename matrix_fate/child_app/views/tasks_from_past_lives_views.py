from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND
from django.shortcuts import get_object_or_404
from drf_spectacular.utils import extend_schema, OpenApiParameter

from common.permissions import IsActivePaidUser

from ..models import ChildCategory, MainTaskSoul, SoulPastExperiencesWithPeople, LessonsFromPastLife
from ..serializers.tasks_from_past_lives_serializers import (
    ChildCategoryFromPastLivesSerializer,
    MainTaskSoulSerializer,
    SoulPastExperiencesWithPeopleSerializer,
    LessonsFromPastLifeSerializer,
)

@extend_schema(tags=["Child Matrix"])
class ChildCategoryWithPastLivesTasksAPIView(APIView):
    """
    Эндпоинт для получения категории (id=5 или title=Задачи, которые тянутся из прошлых жизней) + связанные арканы по order_id.
    """
    permission_classes = [IsActivePaidUser]
    serializer_class = ChildCategoryFromPastLivesSerializer

    @extend_schema(
        parameters=[
            OpenApiParameter(name="arcana_d", description="Аркан (d) - Главная задача Души", required=False, type=int),
            OpenApiParameter(name="arcana_d1", description="Аркан (d1) - Урок из прошлой жизни", required=False, type=int),
            OpenApiParameter(name="arcana_d2", description="Аркан (d2) - Опыт души в прошлом с людьми", required=False, type=int),
        ]
    )
    def get(self, request, category_id_or_title):

        if category_id_or_title.isdigit():
            category = get_object_or_404(ChildCategory, id=int(category_id_or_title))
        else:
            category = get_object_or_404(ChildCategory, title__iexact=category_id_or_title)

        arcana_d_order = request.query_params.get("arcana_d")
        arcana_d1_order = request.query_params.get("arcana_d1")
        arcana_d2_order = request.query_params.get("arcana_d2")

        response_data = {
            "id": category.id,
            "title": category.title,
            "description": category.description,
            "is_paid": category.is_paid,
        }

        if arcana_d_order:
            try:
                arcana_d = MainTaskSoul.objects.get(category=category, order_id=arcana_d_order)
                response_data["arcana_d"] = MainTaskSoulSerializer(arcana_d).data
            except MainTaskSoul.DoesNotExist:
                return Response(
                    {"error": f"Аркан с order_id={arcana_d_order} в MainTaskSoul не найден"},
                    status=HTTP_404_NOT_FOUND,
                )

        if arcana_d1_order:
            try:
                arcana_d1 = LessonsFromPastLife.objects.get(category=category, order_id=arcana_d1_order)
                response_data["arcana_d1"] = LessonsFromPastLifeSerializer(arcana_d1).data
            except LessonsFromPastLife.DoesNotExist:
                return Response(
                    {"error": f"Аркан с order_id={arcana_d1_order} в LessonsFromPastLife не найден"},
                    status=HTTP_404_NOT_FOUND,
                )

        if arcana_d2_order:
            try:
                arcana_d2 = SoulPastExperiencesWithPeople.objects.get(category=category, order_id=arcana_d2_order)
                response_data["arcana_d2"] = SoulPastExperiencesWithPeopleSerializer(arcana_d2).data
            except SoulPastExperiencesWithPeople.DoesNotExist:
                return Response(
                    {"error": f"Аркан с order_id={arcana_d2_order} в SoulPastExperiencesWithPeople не найден"},
                    status=HTTP_404_NOT_FOUND,
                )

        if not arcana_d_order and not arcana_d1_order and not arcana_d2_order:
            return Response(
                {"error": "Необходимо передать хотя бы один order_id аркана (arcana_d, arcana_d1, arcana_d2)"},
                status=HTTP_400_BAD_REQUEST,
            )

        return Response({"category": response_data})
