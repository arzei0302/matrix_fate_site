from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND
from django.shortcuts import get_object_or_404
from drf_spectacular.utils import extend_schema, OpenApiParameter

from matrix_fate.common.permissions import is_active_paid_user

from ..models import (
    CompatibilityCategory,
    CoupleRelations1,
    CoupleRelations2,
    WhatRelationshipProblemsCanArise,
)
from ..serializers.couple_relations_serializers import (
    CompatibilityCategoryCoupleRelationsSerializer,
    CoupleRelations1Serializer,
    CoupleRelations2Serializer,
    WhatRelationshipProblemsCanAriseSerializer,
)
from common.mixins import PaidCategoryAccessMixin


@extend_schema(tags=["Compatibility Matrix"])
class CompatibilityCategoryWithRelationsAPIView(APIView, PaidCategoryAccessMixin):
    """
    Эндпоинт для получения категории(id=7 или title=Отношения в паре) + три связанных аркана по order_id.
    """
    # permission_classes = []
    serializer_class = CompatibilityCategoryCoupleRelationsSerializer

    @extend_schema(
        parameters=[
            OpenApiParameter(
                name="arcana_d2",
                description="Отношения в паре (d2)",
                required=True,
                type=int,
            ),
            OpenApiParameter(
                name="arcana_k",
                description="Отношения в паре (k)",
                required=True,
                type=int,
            ),
            OpenApiParameter(
                name="arcana_j",
                description="Какие могут возникнуть проблемы в отношениях (j)",
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

        arcana_d2_order = request.query_params.get("arcana_d2")
        arcana_k_order = request.query_params.get("arcana_k")
        arcana_j_order = request.query_params.get("arcana_j")

        if not (arcana_d2_order and arcana_k_order and arcana_j_order):
            return Response(
                {
                    "error": "Необходимо передать три числа (arcana_d2, arcana_k, arcana_j)"
                },
                status=HTTP_400_BAD_REQUEST,
            )

        try:
            arcana_d2 = CoupleRelations1.objects.get(
                category=category, order_id=arcana_d2_order
            )
            arcana_k = CoupleRelations2.objects.get(
                category=category, order_id=arcana_k_order
            )
            arcana_j = WhatRelationshipProblemsCanArise.objects.get(
                category=category, order_id=arcana_j_order
            )
        except CoupleRelations1.DoesNotExist:
            return Response(
                {
                    "error": f"Аркан с order_id={arcana_d2_order} в CoupleRelations1 не найден"
                },
                status=HTTP_404_NOT_FOUND,
            )
        except CoupleRelations2.DoesNotExist:
            return Response(
                {
                    "error": f"Аркан с order_id={arcana_k_order} в CoupleRelations2 не найден"
                },
                status=HTTP_404_NOT_FOUND,
            )
        except WhatRelationshipProblemsCanArise.DoesNotExist:
            return Response(
                {
                    "error": f"Аркан с order_id={arcana_j_order} в WhatRelationshipProblemsCanArise не найден"
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
                    "arcana_d2": CoupleRelations1Serializer(arcana_d2).data,
                    "arcana_k": CoupleRelations2Serializer(arcana_k).data,
                    "arcana_j": WhatRelationshipProblemsCanAriseSerializer(
                        arcana_j
                    ).data,
                }
            }
        )
