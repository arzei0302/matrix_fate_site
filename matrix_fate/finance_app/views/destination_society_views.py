from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND
from django.shortcuts import get_object_or_404
from drf_spectacular.utils import extend_schema, OpenApiParameter

from matrix_fate.common.permissions import IsActivePaidUser

from ..models import (
    FinanceCategory,
    TaskPersonalArcana1,
    TaskPersonalArcana2,
    TaskPersonalArcana3,
)
from ..serializers.destination_society_serializers import (
    TaskPersonalArcana1Serializer,
    TaskPersonalArcana2Serializer,
    TaskPersonalArcana3Serializer,
    FinanceCategoryDestinationSocietySerializer,
)


@extend_schema(tags=["Finance Matrix"])
class FinanceCategoryWithTasksAPIView(APIView):
    """
    Эндпоинт для получения категории(id=3 или title=Предназначение для социума) + задачи персональных арканов по order_id.
    """
    permission_classes = [IsActivePaidUser]
    serializer_class = FinanceCategoryDestinationSocietySerializer

    @extend_schema(
        parameters=[
            OpenApiParameter(
                name="task_t",
                description="Задача для персонального аркана1 (t)",
                required=True,
                type=int,
            ),
            OpenApiParameter(
                name="task_u",
                description="Задача для персонального аркана2 (u)",
                required=True,
                type=int,
            ),
            OpenApiParameter(
                name="task_v",
                description="Задача для персонального аркана3 (v)",
                required=True,
                type=int,
            ),
        ]
    )
    def get(self, request, category_id_or_title):

        if category_id_or_title.isdigit():
            category = get_object_or_404(FinanceCategory, id=int(category_id_or_title))
        else:
            category = get_object_or_404(
                FinanceCategory, title__iexact=category_id_or_title
            )

        task_t_order = request.query_params.get("task_t")
        task_u_order = request.query_params.get("task_u")
        task_v_order = request.query_params.get("task_v")

        if not (task_t_order and task_u_order and task_v_order):
            return Response(
                {"error": "Необходимо передать три числа (task_t, task_u, task_v)"},
                status=HTTP_400_BAD_REQUEST,
            )

        try:
            task_t = TaskPersonalArcana1.objects.get(
                category=category, order_id=task_t_order
            )
            task_u = TaskPersonalArcana2.objects.get(
                category=category, order_id=task_u_order
            )
            task_v = TaskPersonalArcana3.objects.get(
                category=category, order_id=task_v_order
            )
        except TaskPersonalArcana1.DoesNotExist:
            return Response(
                {
                    "error": f"Задача с order_id={task_t_order} в TaskPersonalArcana1 не найдена"
                },
                status=HTTP_404_NOT_FOUND,
            )
        except TaskPersonalArcana2.DoesNotExist:
            return Response(
                {
                    "error": f"Задача с order_id={task_u_order} в TaskPersonalArcana2 не найдена"
                },
                status=HTTP_404_NOT_FOUND,
            )
        except TaskPersonalArcana3.DoesNotExist:
            return Response(
                {
                    "error": f"Задача с order_id={task_v_order} в TaskPersonalArcana3 не найдена"
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
                    "task_t": TaskPersonalArcana1Serializer(task_t).data,
                    "task_u": TaskPersonalArcana2Serializer(task_u).data,
                    "task_v": TaskPersonalArcana3Serializer(task_v).data,
                }
            }
        )
