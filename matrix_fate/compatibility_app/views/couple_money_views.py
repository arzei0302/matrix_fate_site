from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND
from django.shortcuts import get_object_or_404
from drf_spectacular.utils import extend_schema, OpenApiParameter

from matrix_fate.common.permissions import is_active_paid_user

from ..models import (
    CompatibilityCategory,
    WhatGivesTribute,
    WhatTasksUnlockMoneyChannels,
    WhatBlocksMonetaryEnergy,
)
from ..serializers.couple_money_serializers import (
    CompatibilityCategoryCoupleMoneySerializer,
    WhatGivesTributeSerializer,
    WhatTasksUnlockMoneyChannelsSerializer,
    WhatBlocksMonetaryEnergySerializer,
)


@extend_schema(tags=["Compatibility Matrix"])
class CompatibilityCategoryWithCoupleMoneyAPIView(APIView):
    """
    Эндпоинт для получения категории(id=6 или title=Деньги в паре) + три связанных аркана по order_id.
    """
    # permission_classes = []
    serializer_class = CompatibilityCategoryCoupleMoneySerializer

    @extend_schema(
        parameters=[
            OpenApiParameter(
                name="arcana_c2",
                description="Что дает деньги (c2)",
                required=True,
                type=int,
            ),
            OpenApiParameter(
                name="arcana_l",
                description="Какие нужно проработать задачи, чтобы раскрыть денежный канал: (l)",
                required=True,
                type=int,
            ),
            OpenApiParameter(
                name="arcana_j",
                description="Что блокирует денежную энергию: (j)",
                required=True,
                type=int,
            ),
        ]
    )
    def get(self, request, category_id_or_title):

        if category_id_or_title.isdigit():
            category = get_object_or_404(
                CompatibilityCategory, id=int(category_id_or_title)
            )
        else:
            category = get_object_or_404(
                CompatibilityCategory, title__iexact=category_id_or_title
            )
        if not is_active_paid_user(request.user):
            return Response({
                "category": {
                    "id": category.id,
                    "title": category.title,
                }
            })

        arcana_c2_order = request.query_params.get("arcana_c2")
        arcana_l_order = request.query_params.get("arcana_l")
        arcana_j_order = request.query_params.get("arcana_j")

        if not (arcana_c2_order and arcana_l_order and arcana_j_order):
            return Response(
                {
                    "error": "Необходимо передать три числа (arcana_c2, arcana_l, arcana_j)"
                },
                status=HTTP_400_BAD_REQUEST,
            )

        try:
            arcana_c2 = WhatGivesTribute.objects.get(
                category=category, order_id=arcana_c2_order
            )
            arcana_l = WhatTasksUnlockMoneyChannels.objects.get(
                category=category, order_id=arcana_j_order
            )
            arcana_j = WhatBlocksMonetaryEnergy.objects.get(
                category=category, order_id=arcana_j_order
            )
        except WhatGivesTribute.DoesNotExist:
            return Response(
                {
                    "error": f"Аркан с order_id={arcana_c2_order} в WhatGivesTribute не найден"
                },
                status=HTTP_404_NOT_FOUND,
            )
        except WhatTasksUnlockMoneyChannels.DoesNotExist:
            return Response(
                {
                    "error": f"Аркан с order_id={arcana_l_order} в WhatTasksUnlockMoneyChannels не найден"
                },
                status=HTTP_404_NOT_FOUND,
            )
        except WhatBlocksMonetaryEnergy.DoesNotExist:
            return Response(
                {
                    "error": f"Аркан с order_id={arcana_j_order} в WhatBlocksMonetaryEnergy не найден"
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
                    "arcana_c2": WhatGivesTributeSerializer(arcana_c2).data,
                    "arcana_l": WhatTasksUnlockMoneyChannelsSerializer(arcana_l).data,
                    "arcana_j": WhatBlocksMonetaryEnergySerializer(arcana_j).data,
                }
            }
        )
