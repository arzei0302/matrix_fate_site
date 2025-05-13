from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND
from django.shortcuts import get_object_or_404
from drf_spectacular.utils import extend_schema, OpenApiParameter

from matrix_fate.common.permissions import is_active_paid_user

# from matrix_fate.common.permissions import IsActivePaidUser

from ..models import (
    FinanceCategory,
    TheMainTask40Years,
    WhatBeforeYouTurn40Years,
    WhatAfterYouTurn40Years,
)
from ..serializers.karma_and_task_40_serializers import (
    FinanceCategorySerializer,
    TheMainTask40YearsSerializer,
    WhatBeforeYouTurn40YearsSerializer,
    WhatAfterYouTurn40YearsSerializer,
)
from matrix_fate.common.mixins import PaidCategoryAccessMixin


@extend_schema(tags=["Finance Matrix"])
class FinanceCategoryWithKarmaAndTask40APIView(APIView, PaidCategoryAccessMixin):
    """
    Эндпоинт для получения категории (id=6 или title=Карма и задача 40 лет) + связанные арканы по order_id.
    """
    # permission_classes = [IsActivePaidUser]
    serializer_class = FinanceCategorySerializer

    @extend_schema(
        parameters=[
            OpenApiParameter(name="arcana_c", description="Аркан (c) - Главная задача 40 лет", required=False, type=int),
            OpenApiParameter(name="arcana_c1", description="Аркан (c1) - Что нужно сделать до 40 лет", required=False, type=int),
            OpenApiParameter(name="arcana_c2", description="Аркан (c2) - Что нужно сделать после 40 лет", required=False, type=int),
        ]
    )
    def get(self, request, category_id_or_title):

        if category_id_or_title.isdigit():
            category = get_object_or_404(FinanceCategory, id=int(category_id_or_title))
        else:
            category = get_object_or_404(FinanceCategory, title__iexact=category_id_or_title)

        access_response = self.check_category_access(request, category)
        if access_response:
            return access_response

        arcana_c_order = request.query_params.get("arcana_c")
        arcana_c1_order = request.query_params.get("arcana_c1")
        arcana_c2_order = request.query_params.get("arcana_c2")

        response_data = {
            "id": category.id,
            "title": category.title,
            "description": category.description,
            "is_paid": category.is_paid,
        }

        if arcana_c_order:
            try:
                arcana_c = TheMainTask40Years.objects.get(category=category, order_id=arcana_c_order)
                response_data["arcana_c"] = TheMainTask40YearsSerializer(arcana_c).data
            except TheMainTask40Years.DoesNotExist:
                return Response(
                    {"error": f"Аркан с order_id={arcana_c_order} в TheMainTask40Years не найден"},
                    status=HTTP_404_NOT_FOUND,
                )

        if arcana_c1_order:
            try:
                arcana_c1 = WhatBeforeYouTurn40Years.objects.get(category=category, order_id=arcana_c1_order)
                response_data["arcana_c1"] = WhatBeforeYouTurn40YearsSerializer(arcana_c1).data
            except WhatBeforeYouTurn40Years.DoesNotExist:
                return Response(
                    {"error": f"Аркан с order_id={arcana_c1_order} в WhatBeforeYouTurn40Years не найден"},
                    status=HTTP_404_NOT_FOUND,
                )

        if arcana_c2_order:
            try:
                arcana_c2 = WhatAfterYouTurn40Years.objects.get(category=category, order_id=arcana_c2_order)
                response_data["arcana_c2"] = WhatAfterYouTurn40YearsSerializer(arcana_c2).data
            except WhatAfterYouTurn40Years.DoesNotExist:
                return Response(
                    {"error": f"Аркан с order_id={arcana_c2_order} в WhatAfterYouTurn40Years не найден"},
                    status=HTTP_404_NOT_FOUND,
                )

        if not arcana_c_order and not arcana_c1_order and not arcana_c2_order:
            return Response(
                {"error": "Необходимо передать хотя бы один order_id аркана (arcana_c, arcana_c1, arcana_c2)"},
                status=HTTP_400_BAD_REQUEST,
            )

        return Response({"category": response_data})
