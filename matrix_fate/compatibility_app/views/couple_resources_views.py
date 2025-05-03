from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND
from django.shortcuts import get_object_or_404
from drf_spectacular.utils import extend_schema, OpenApiParameter

from matrix_fate.common.permissions import is_active_paid_user

from ..models import (
    CompatibilityCategory,
    CoupleResourcesArcana1,
    CoupleResourcesArcana2,
)
from ..serializers.couple_resources_serializers import (
    CompatibilityCategoryCoupleResourcesSerializer,
    CoupleResourcesArcana1Serializer,
    CoupleResourcesArcana2Serializer,
)


@extend_schema(tags=["Compatibility Matrix"])
class CompatibilityCategoryWithResourcesAPIView(APIView):
    """
    Эндпоинт для получения категории(id=3 или title=Ресурсы пары) + два связанных аркана по order_id.
    """
    # permission_classes = []
    serializer_class = CompatibilityCategoryCoupleResourcesSerializer

    @extend_schema(
        parameters=[
            OpenApiParameter(
                name="arcana_b", description="Ресурсы пары (b)", required=True, type=int
            ),
            OpenApiParameter(
                name="arcana_c", description="Ресурсы пары (c)", required=True, type=int
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

        arcana_b_order = request.query_params.get("arcana_b")
        arcana_c_order = request.query_params.get("arcana_c")

        if not (arcana_b_order and arcana_c_order):
            return Response(
                {"error": "Необходимо передать два числа (arcana_b, arcana_c)"},
                status=HTTP_400_BAD_REQUEST,
            )

        try:
            arcana_b = CoupleResourcesArcana1.objects.get(
                category=category, order_id=arcana_b_order
            )
            arcana_c = CoupleResourcesArcana2.objects.get(
                category=category, order_id=arcana_c_order
            )
        except CoupleResourcesArcana1.DoesNotExist:
            return Response(
                {
                    "error": f"Аркан с order_id={arcana_b_order} в CoupleResourcesArcana1 не найден"
                },
                status=HTTP_404_NOT_FOUND,
            )
        except CoupleResourcesArcana2.DoesNotExist:
            return Response(
                {
                    "error": f"Аркан с order_id={arcana_c_order} в CoupleResourcesArcana2 не найден"
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
                    "arcana_b": CoupleResourcesArcana1Serializer(arcana_b).data,
                    "arcana_c": CoupleResourcesArcana2Serializer(arcana_c).data,
                }
            }
        )
