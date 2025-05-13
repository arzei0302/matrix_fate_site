from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND
from django.shortcuts import get_object_or_404
from drf_spectacular.utils import extend_schema, OpenApiParameter

from matrix_fate.common.permissions import is_active_paid_user

from ..models import CompatibilityCategory, WhatFillsTheVapor
from ..serializers.what_fills_the_vapor_serializers import (
    CompatibilityCategoryWhatFillsSerializer,
    WhatFillsTheVaporSerializer,
)
from common.mixins import PaidCategoryAccessMixin


@extend_schema(tags=["Compatibility Matrix"])
class CompatibilityCategoryWithWhatFillsAPIView(APIView, PaidCategoryAccessMixin):
    """
    Эндпоинт для получения категории(id=4 или title=От чего наполняется пара) + аркан по order_id.
    """
    # permission_classes = []
    serializer_class = CompatibilityCategoryWhatFillsSerializer

    @extend_schema(
        parameters=[
            OpenApiParameter(
                name="arcana_e",
                description="От чего наполняется пара (e)",
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

        # ✅ проверка доступа через миксин
        access_response = self.check_category_access(request, category)
        if access_response:
            return access_response

        arcana_e_order = request.query_params.get("arcana_e")

        if not arcana_e_order:
            return Response(
                {"error": "Необходимо передать order_id аркана (arcana_e)"},
                status=HTTP_400_BAD_REQUEST,
            )

        try:
            arcana_e = WhatFillsTheVapor.objects.get(
                category=category, order_id=arcana_e_order
            )
        except WhatFillsTheVapor.DoesNotExist:
            return Response(
                {
                    "error": f"Аркан с order_id={arcana_e_order} в WhatFillsTheVapor не найден"
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
                    "arcana_e": WhatFillsTheVaporSerializer(arcana_e).data,
                }
            }
        )
