from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND
from django.shortcuts import get_object_or_404
from drf_spectacular.utils import extend_schema, OpenApiParameter

from matrix_fate.common.permissions import is_active_paid_user

# from matrix_fate.common.permissions import IsActivePaidUser

from ..models import (
    Category,
    SuitableProfessions,
    MoneySources,
    MoneyGrowthTasks1,
    MoneyGrowthTasks2,
    MoneyBlocks,
    MoneyUnblock,
)
from ..serializers.matrix_money_serializers import (
    CategoryWithMatrixMoneySerializer,
    SuitableProfessionsSerializer,
    MoneySourcesSerializer,
    MoneyGrowthTasks1Serializer,
    MoneyGrowthTasks2Serializer,
    MoneyBlocksSerializer,
    MoneyUnblockSerializer,
)


@extend_schema(tags=["Matrix_Fate"])
class CategoryWithMatrixMoneyAPIView(GenericAPIView):
    """Получает категорию по `id(15)` или `title(Деньги в матрице)` и арканы по переданным order_id."""

    # permission_classes = [IsActivePaidUser]
    serializer_class = CategoryWithMatrixMoneySerializer

    @extend_schema(
        parameters=[
            OpenApiParameter(
                name="professions",
                description="Какие подходят профессии (c2)",
                required=True,
                type=int,
            ),
            OpenApiParameter(
                name="money",
                description="Что дает деньги (l)",
                required=True,
                type=int,
            ),
            OpenApiParameter(
                name="tasks1",
                description="Какие задачи раскрывают денежный канал (l)",
                required=True,
                type=int,
            ),
            OpenApiParameter(
                name="tasks2",
                description="Какие задачи раскрывают денежный канал (c2)",
                required=True,
                type=int,
            ),
            OpenApiParameter(
                name="blocks",
                description="Что блокирует денежную энергию (j)",
                required=True,
                type=int,
            ),
            OpenApiParameter(
                name="unblock",
                description="Что помогает раскрыть деньги (j)",
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

        if not is_active_paid_user(request.user):
            return Response({
                "category": {
                    "id": category.id,
                    "title": category.title,
                }
            })

        order_params = {
            "professions": (SuitableProfessions, SuitableProfessionsSerializer),
            "money": (MoneySources, MoneySourcesSerializer),
            "tasks1": (MoneyGrowthTasks1, MoneyGrowthTasks1Serializer),
            "tasks2": (MoneyGrowthTasks2, MoneyGrowthTasks2Serializer),
            "blocks": (MoneyBlocks, MoneyBlocksSerializer),
            "unblock": (MoneyUnblock, MoneyUnblockSerializer),
        }
        response_data = {
            "category": {
                "id": category.id,
                "title": category.title,
                "description": category.description,
                "is_paid": category.is_paid,
            }
        }

        for param, (model, serializer_class) in order_params.items():
            order_id = request.query_params.get(param)
            if not order_id:
                return Response(
                    {"error": f"Параметр {param} обязателен"},
                    status=HTTP_400_BAD_REQUEST,
                )
            try:
                instance = model.objects.get(category=category, order_id=order_id)
                response_data[param] = serializer_class(instance).data
            except model.DoesNotExist:
                return Response(
                    {"error": f"{param} с order_id={order_id} не найден"},
                    status=HTTP_404_NOT_FOUND,
                )

        return Response(response_data)
