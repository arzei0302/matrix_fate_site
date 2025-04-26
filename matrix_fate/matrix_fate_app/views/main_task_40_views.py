from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND
from django.shortcuts import get_object_or_404
from drf_spectacular.utils import extend_schema, OpenApiParameter

from matrix_fate.common.permissions import IsActivePaidUser

from ..models import Category, MainTask40, TaskBefore40, TaskAfter40
from ..serializers.main_task_40_serializers import (
    CategoryMainTask40Serializer,
    MainTask40Serializer,
    TaskBefore40Serializer,
    TaskAfter40Serializer,
)


@extend_schema(tags=["Matrix_Fate"])
class CategoryWithMainTask40APIView(APIView):
    """Получает категорию(id=6) или title(Карма и задача 40 лет) и таланты по переданным `order_id`."""

    permission_classes = [IsActivePaidUser]
    serializer_class = CategoryMainTask40Serializer


    @extend_schema(
        parameters=[
            OpenApiParameter(
                name="main",
                description="Главная задача 40 лет (d)",
                required=True,
                type=int,
            ),
            OpenApiParameter(
                name="before",
                description="Что нужно сделать до 40 лет (d1)",
                required=True,
                type=int,
            ),
            OpenApiParameter(
                name="after",
                description="Что нужно сделать после 40 лет (d2)",
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

        main_order = request.query_params.get("main")
        before_order = request.query_params.get("before")
        after_order = request.query_params.get("after")

        if not (main_order and before_order and after_order):
            return Response(
                {"error": "Необходимо передать три числа (main, before, after)"},
                status=HTTP_400_BAD_REQUEST,
            )

        try:
            main_task = MainTask40.objects.get(category=category, order_id=main_order)
            before_task = TaskBefore40.objects.get(
                category=category, order_id=before_order
            )
            after_task = TaskAfter40.objects.get(
                category=category, order_id=after_order
            )
        except MainTask40.DoesNotExist:
            return Response(
                {"error": f"Задача с order_id={main_order} в MainTask40 не найдена"},
                status=HTTP_404_NOT_FOUND,
            )
        except TaskBefore40.DoesNotExist:
            return Response(
                {
                    "error": f"Задача с order_id={before_order} в TaskBefore40 не найдена"
                },
                status=HTTP_404_NOT_FOUND,
            )
        except TaskAfter40.DoesNotExist:
            return Response(
                {"error": f"Задача с order_id={after_order} в TaskAfter40 не найдена"},
                status=HTTP_404_NOT_FOUND,
            )

        return Response(
            {
                "category": {
                    "id": category.id,
                    "title": category.title,
                    "description": category.description,
                    "is_paid": category.is_paid,
                    "main_task": MainTask40Serializer(main_task).data,
                    "task_before_40": TaskBefore40Serializer(before_task).data,
                    "task_after_40": TaskAfter40Serializer(after_task).data,
                }
            }
        )
