from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND
from django.shortcuts import get_object_or_404
from drf_spectacular.utils import extend_schema, OpenApiParameter

from matrix_fate.common.permissions import is_active_paid_user

# from matrix_fate.common.permissions import IsActivePaidUser

from ..models import (
    FinanceCategory,
    TasksOpenMoneyChannel1,
    TasksOpenMoneyChannel2,
    WhatBlocksMoneyEnergy,
)
from ..serializers.what_blocks_money_energy_serializers import (
    FinanceCategoryBlocksMoneySerializer,
    TasksOpenMoneyChannel1Serializer,
    TasksOpenMoneyChannel2Serializer,
    WhatBlocksMoneyEnergySerializer,
)


@extend_schema(tags=["Finance Matrix"])
class FinanceCategoryWithBlocksAPIView(APIView):
    """
    Эндпоинт для получения категории(id=5 или title=Что блокирует денежную энергию) + три связанных аркана по order_id.
    """

    # permission_classes = [IsActivePaidUser]
    serializer_class = FinanceCategoryBlocksMoneySerializer

    @extend_schema(
        parameters=[
            OpenApiParameter(
                name="task_l",
                description="Какие нужно проработать задачи, чтобы раскрыть денежный канал: (l)",
                required=True,
                type=int,
            ),
            OpenApiParameter(
                name="task_c2",
                description="Какие нужно проработать задачи, чтобы раскрыть денежный канал: (c2)",
                required=True,
                type=int,
            ),
            OpenApiParameter(
                name="block_j",
                description="Что блокирует денежную энергию: (j)",
                required=True,
                type=int,
            ),
        ]
    )
    def get(self, request, category_id_or_title):
        """Получает категорию по `id(5)` или `title(Что блокирует денежную энергию)` и три аркана из таблиц по переданным номерам (order_id)."""

        if category_id_or_title.isdigit():
            category = get_object_or_404(FinanceCategory, id=int(category_id_or_title))
        else:
            category = get_object_or_404(
                FinanceCategory, title__iexact=category_id_or_title
            )

        if not is_active_paid_user(request.user):
            return Response({
                "category": {
                    "id": category.id,
                    "title": category.title,
                }
            })

        task_l_order = request.query_params.get("task_l")
        task_c2_order = request.query_params.get("task_c2")
        block_j_order = request.query_params.get("block_j")

        if not (task_l_order and task_c2_order and block_j_order):
            return Response(
                {"error": "Необходимо передать три числа (task_i1, task_c2, block_k)"},
                status=HTTP_400_BAD_REQUEST,
            )

        try:
            task_l = TasksOpenMoneyChannel1.objects.get(
                category=category, order_id=task_l_order
            )
            task_c2 = TasksOpenMoneyChannel2.objects.get(
                category=category, order_id=task_c2_order
            )
            block_j = WhatBlocksMoneyEnergy.objects.get(
                category=category, order_id=block_j_order
            )
        except TasksOpenMoneyChannel1.DoesNotExist:
            return Response(
                {
                    "error": f"Задача с order_id={task_l_order} в TasksOpenMoneyChannel1 не найдена"
                },
                status=HTTP_404_NOT_FOUND,
            )
        except TasksOpenMoneyChannel2.DoesNotExist:
            return Response(
                {
                    "error": f"Задача с order_id={task_c2_order} в TasksOpenMoneyChannel2 не найдена"
                },
                status=HTTP_404_NOT_FOUND,
            )
        except WhatBlocksMoneyEnergy.DoesNotExist:
            return Response(
                {
                    "error": f"Задача с order_id={block_j_order} в WhatBlocksMoneyEnergy не найдена"
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
                    "task_l": TasksOpenMoneyChannel1Serializer(task_l).data,
                    "task_c2": TasksOpenMoneyChannel2Serializer(task_c2).data,
                    "block_j": WhatBlocksMoneyEnergySerializer(block_j).data,
                }
            }
        )
