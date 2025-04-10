from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND
from django.shortcuts import get_object_or_404
from drf_spectacular.utils import extend_schema, OpenApiParameter

from common.permissions import IsActivePaidUser

from ..models import (
    CompatibilityCategory,
    TasksForCoupleArcana1,
    TasksForCoupleArcana2,
    TasksForCoupleArcana3,
)
from ..serializers.tasks_for_couple_serializers import (
    CompatibilityCategoryTasksForCoupleSerializer,
    TasksForCoupleArcana1Serializer,
    TasksForCoupleArcana2Serializer,
    TasksForCoupleArcana3Serializer,
)


@extend_schema(tags=["Compatibility Matrix"])
class CompatibilityCategoryWithTasksAPIView(APIView):
    """
    Эндпоинт для получения категории(id=2 или title=Задачи для пары) + три связанных аркана по order_id.
    """
    # permission_classes = [IsActivePaidUser]
    serializer_class = CompatibilityCategoryTasksForCoupleSerializer

    @extend_schema(
        parameters=[
            OpenApiParameter(
                name="arcana_w",
                description="Задача для пары (w)",
                required=True,
                type=int,
            ),
            OpenApiParameter(
                name="arcana_d",
                description="Задача для пары (d)",
                required=True,
                type=int,
            ),
            OpenApiParameter(
                name="arcana_y",
                description="Задача для пары (y)",
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

        arcana_w_order = request.query_params.get("arcana_w")
        arcana_d_order = request.query_params.get("arcana_d")
        arcana_y_order = request.query_params.get("arcana_y")

        if not (arcana_w_order and arcana_d_order and arcana_y_order):
            return Response(
                {
                    "error": "Необходимо передать три числа (arcana_w, arcana_d, arcana_y)"
                },
                status=HTTP_400_BAD_REQUEST,
            )

        try:
            arcana_w = TasksForCoupleArcana1.objects.get(
                category=category, order_id=arcana_w_order
            )
            arcana_d = TasksForCoupleArcana2.objects.get(
                category=category, order_id=arcana_d_order
            )
            arcana_y = TasksForCoupleArcana3.objects.get(
                category=category, order_id=arcana_y_order
            )
        except TasksForCoupleArcana1.DoesNotExist:
            return Response(
                {
                    "error": f"Аркан с order_id={arcana_w_order} в TasksForCoupleArcana1 не найден"
                },
                status=HTTP_404_NOT_FOUND,
            )
        except TasksForCoupleArcana2.DoesNotExist:
            return Response(
                {
                    "error": f"Аркан с order_id={arcana_d_order} в TasksForCoupleArcana2 не найден"
                },
                status=HTTP_404_NOT_FOUND,
            )
        except TasksForCoupleArcana3.DoesNotExist:
            return Response(
                {
                    "error": f"Аркан с order_id={arcana_y_order} в TasksForCoupleArcana3 не найден"
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
                    "arcana_w": TasksForCoupleArcana1Serializer(arcana_w).data,
                    "arcana_d": TasksForCoupleArcana2Serializer(arcana_d).data,
                    "arcana_y": TasksForCoupleArcana3Serializer(arcana_y).data,
                }
            }
        )
