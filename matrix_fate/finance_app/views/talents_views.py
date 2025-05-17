from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND
from django.shortcuts import get_object_or_404
from drf_spectacular.utils import extend_schema, OpenApiParameter

# from matrix_fate.common.permissions import is_active_paid_user

# from matrix_fate.common.permissions import IsActivePaidUser

from ..models import (
    FinanceCategory,
    QualitiesDevelopAge40,
    QualitiesRevealedAge20,
    YourGreatestTalentBirth,
)
from ..serializers.talents_serializers import (
    QualitiesDevelopAge40Serializer,
    QualitiesRevealedAge20Serializer,
    YourGreatestTalentBirthSerializer,
    FinanceCategoryTalentsSerializer,
)
from matrix_fate.common.mixins import PaidCategoryAccessMixin


@extend_schema(tags=["Finance Matrix"])
class FinanceCategoryWithTalentsAPIView(APIView, PaidCategoryAccessMixin):
    """
    Эндпоинт для получения категории(id=1 или title=Таланты) + связанные арканы по их order_id.
    """
    # permission_classes = [IsActivePaidUser]
    serializer_class = FinanceCategoryTalentsSerializer

    @extend_schema(
        parameters=[
            OpenApiParameter(
                name="birth_a",
                description="Талант при рождении(a)",
                required=True,
                type=int,
            ),
            OpenApiParameter(
                name="youth_b",
                description="Качества к 20 годам(b)",
                required=True,
                type=int,
            ),
            OpenApiParameter(
                name="mature_c",
                description="Качества к 40 годам(c)",
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

        access_response = self.check_category_access(request, category)
        if access_response:
            return access_response

        birth_order = request.query_params.get("birth_a")
        youth_order = request.query_params.get("youth_b")
        mature_order = request.query_params.get("mature_c")

        if not (birth_order and youth_order and mature_order):
            return Response(
                {"error": "Необходимо передать три числа (birth, youth, mature)"},
                status=HTTP_400_BAD_REQUEST,
            )

        try:
            birth_talent = YourGreatestTalentBirth.objects.get(
                category=category, order_id=birth_order
            )
            youth_talent = QualitiesRevealedAge20.objects.get(
                category=category, order_id=youth_order
            )
            mature_talent = QualitiesDevelopAge40.objects.get(
                category=category, order_id=mature_order
            )
        except YourGreatestTalentBirth.DoesNotExist:
            return Response(
                {
                    "error": f"Талант с order_id={birth_order} в YourGreatestTalentBirth не найден"
                },
                status=HTTP_404_NOT_FOUND,
            )
        except QualitiesRevealedAge20.DoesNotExist:
            return Response(
                {
                    "error": f"Талант с order_id={youth_order} в QualitiesRevealedAge20 не найден"
                },
                status=HTTP_404_NOT_FOUND,
            )
        except QualitiesDevelopAge40.DoesNotExist:
            return Response(
                {
                    "error": f"Талант с order_id={mature_order} в QualitiesDevelopAge40 не найден"
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
                    "birth_talent": YourGreatestTalentBirthSerializer(
                        birth_talent
                    ).data,
                    "youth_talent": QualitiesRevealedAge20Serializer(youth_talent).data,
                    "mature_talent": QualitiesDevelopAge40Serializer(
                        mature_talent
                    ).data,
                }
            }
        )
