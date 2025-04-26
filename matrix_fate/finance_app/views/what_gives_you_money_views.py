from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND
from django.shortcuts import get_object_or_404
from drf_spectacular.utils import extend_schema, OpenApiParameter

from matrix_fate.common.permissions import IsActivePaidUser

from ..models import (
    FinanceCategory,
    WhatGivesYouMoney,
    WhatOpensYourMoneyChannel,
    AreasOfRealization,
)
from ..serializers.what_gives_you_money_serializers import (
    WhatGivesYouMoneySerializer,
    WhatOpensYourMoneyChannelSerializer,
    AreasOfRealizationSerializer,
    FinanceCategoryWhatGivesYouMoneySerializer
)


@extend_schema(tags=["Finance Matrix"])
class FinanceCategoryWhatGivesYouMoneyAPIView(APIView):
    """
    Эндпоинт для получения категории(id=4 или title=Что дает деньги) + три связанных аркана по order_id.
    """

    permission_classes = [IsActivePaidUser]
    serializer_class = FinanceCategoryWhatGivesYouMoneySerializer

    @extend_schema(
        parameters=[
            OpenApiParameter(
                name="money_j",
                description="Что дает деньги (j)",
                required=True,
                type=int,
            ),
            OpenApiParameter(
                name="money_channel_l",
                description="Что открывает ваш денежный канал (l)",
                required=True,
                type=int,
            ),
            OpenApiParameter(
                name="realization_c2",
                description="Сферы реализации (c2)",
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

        money_order = request.query_params.get("money_j")
        money_channel_order = request.query_params.get("money_channel_l")
        realization_order = request.query_params.get("realization_c2")

        if not (money_order and money_channel_order and realization_order):
            return Response(
                {
                    "error": "Необходимо передать три числа (money_j, money_channel_l, realization_c2)"
                },
                status=HTTP_400_BAD_REQUEST,
            )

        try:
            money = WhatGivesYouMoney.objects.get(
                category=category, order_id=money_order
            )
            money_channel = WhatOpensYourMoneyChannel.objects.get(
                category=category, order_id=money_channel_order
            )
            realization = AreasOfRealization.objects.get(
                category=category, order_id=realization_order
            )
        except WhatGivesYouMoney.DoesNotExist:
            return Response(
                {
                    "error": f"Запись с order_id={money_order} в WhatGivesYouMoney не найдена"
                },
                status=HTTP_404_NOT_FOUND,
            )
        except WhatOpensYourMoneyChannel.DoesNotExist:
            return Response(
                {
                    "error": f"Запись с order_id={money_channel_order} в WhatOpensYourMoneyChannel не найдена"
                },
                status=HTTP_404_NOT_FOUND,
            )
        except AreasOfRealization.DoesNotExist:
            return Response(
                {
                    "error": f"Запись с order_id={realization_order} в AreasOfRealization не найдена"
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
                    "money": WhatGivesYouMoneySerializer(money).data,
                    "money_channel": WhatOpensYourMoneyChannelSerializer(
                        money_channel
                    ).data,
                    "realization": AreasOfRealizationSerializer(realization).data,
                }
            }
        )
