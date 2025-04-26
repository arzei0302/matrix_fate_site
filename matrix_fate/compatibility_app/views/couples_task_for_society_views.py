from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND
from django.shortcuts import get_object_or_404
from drf_spectacular.utils import extend_schema, OpenApiParameter

from matrix_fate.common.permissions import IsActivePaidUser

from ..models import CompatibilityCategory, CouplesTaskForSociety
from ..serializers.couples_task_for_society_serializers import (
    CompatibilityCategoryCouplesTaskSerializer,
    CouplesTaskForSocietySerializer,
)


@extend_schema(tags=["Compatibility Matrix"])
class CompatibilityCategoryWithCouplesTaskAPIView(APIView):
    """
    Эндпоинт для получения категории(id=5 или title=Задача пары для социума) + аркан по order_id.
    """

    permission_classes = [IsActivePaidUser]
    serializer_class = CompatibilityCategoryCouplesTaskSerializer

    @extend_schema(
        parameters=[
            OpenApiParameter(
                name="arcana_v",
                description="Задача пары для социума (v)",
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

        arcana_v_order = request.query_params.get("arcana_v")

        if not arcana_v_order:
            return Response(
                {"error": "Необходимо передать order_id аркана (arcana_v)"},
                status=HTTP_400_BAD_REQUEST,
            )

        try:
            arcana_v = CouplesTaskForSociety.objects.get(
                category=category, order_id=arcana_v_order
            )
        except CouplesTaskForSociety.DoesNotExist:
            return Response(
                {
                    "error": f"Аркан с order_id={arcana_v_order} в CouplesTaskForSociety не найден"
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
                    "arcana_v": CouplesTaskForSocietySerializer(arcana_v).data,
                }
            }
        )
