from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND
from django.shortcuts import get_object_or_404
from drf_spectacular.utils import extend_schema, OpenApiParameter

from matrix_fate.common.permissions import is_active_paid_user

from ..models import Category, SpiritualTask1, SpiritualTask2, SpiritualTask3
from ..serializers.spiritual_karma_serializers import (
    CategoryWithSpiritualKarmaSerializer,
    SpiritualTask1Serializer,
    SpiritualTask2Serializer,
    SpiritualTask3Serializer,
)
from matrix_fate.common.mixins import PaidCategoryAccessMixin


@extend_schema(tags=["Matrix_Fate"])
class CategoryWithSpiritualKarmaAPIView(APIView, PaidCategoryAccessMixin):
    """Получает категорию по `id(13)` или `title(Духовная карма)` и три задачи духовной кармы по переданным order_id."""

    permission_classes = []  # ВАЖНО: убираем пермишены!

    @extend_schema(
        parameters=[
            OpenApiParameter(
                name="task1",
                description="Духовная задача 1 (b)",
                required=True,
                type=int,
            ),
            OpenApiParameter(
                name="task2",
                description="Духовная задача 2 (b1)",
                required=True,
                type=int,
            ),
            OpenApiParameter(
                name="task3",
                description="Духовная задача 3 (b2)",
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

        task1_order = request.query_params.get("task1")
        task2_order = request.query_params.get("task2")
        task3_order = request.query_params.get("task3")

        if not (task1_order and task2_order and task3_order):
            return Response(
                {"error": "Необходимо передать три числа (task1, task2, task3)"},
                status=HTTP_400_BAD_REQUEST,
            )

        try:
            task1 = SpiritualTask1.objects.get(category=category, order_id=task1_order)
            task2 = SpiritualTask2.objects.get(category=category, order_id=task2_order)
            task3 = SpiritualTask3.objects.get(category=category, order_id=task3_order)
        except SpiritualTask1.DoesNotExist:
            return Response(
                {"error": f"Задача 1 с order_id={task1_order} не найдена"},
                status=HTTP_404_NOT_FOUND,
            )
        except SpiritualTask2.DoesNotExist:
            return Response(
                {"error": f"Задача 2 с order_id={task2_order} не найдена"},
                status=HTTP_404_NOT_FOUND,
            )
        except SpiritualTask3.DoesNotExist:
            return Response(
                {"error": f"Задача 3 с order_id={task3_order} не найдена"},
                status=HTTP_404_NOT_FOUND,
            )

        return Response({
            "category": {
                "id": category.id,
                "title": category.title,
                "description": category.description,
                "is_paid": category.is_paid,
                "spiritual_task_1": SpiritualTask1Serializer(task1).data,
                "spiritual_task_2": SpiritualTask2Serializer(task2).data,
                "spiritual_task_3": SpiritualTask3Serializer(task3).data,
            }
        })
