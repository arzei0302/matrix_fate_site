from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND
from django.shortcuts import get_object_or_404
from drf_spectacular.utils import extend_schema, OpenApiParameter

from common.permissions import IsActivePaidUser

from ..models import Category, InnateTalent, QualitiesRevealed, QualitiesDeveloped
from ..serializers.soul_work_serializers import (
    CategorySoulWorkSerializer,
    InnateTalentSerializer,
    QualitiesRevealedSerializer,
    QualitiesDevelopedSerializer,
)

@extend_schema(tags=["Matrix_Fate"])
class CategoryWithTalentsSoulAPIView(APIView):
    """Получает категорию(id=5) или title(Кем работать для души) и таланты по переданным `order_id`."""
    
    permission_classes = [IsActivePaidUser]
    serializer_class = CategorySoulWorkSerializer

    @extend_schema(
        parameters=[
            OpenApiParameter(
                name="innate",
                description="Талант от рождения (a)",
                required=True,
                type=int,
            ),
            OpenApiParameter(
                name="revealed",
                description="Качества к 20 годам (b)",
                required=True,
                type=int,
            ),
            OpenApiParameter(
                name="developed",
                description="Качества к 40 годам (c)",
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

        innate_order = request.query_params.get("innate")
        revealed_order = request.query_params.get("revealed")
        developed_order = request.query_params.get("developed")

        if not (innate_order and revealed_order and developed_order):
            return Response(
                {
                    "error": "Необходимо передать три числа (innate, revealed, developed)"
                },
                status=HTTP_400_BAD_REQUEST,
            )

        try:
            innate_talent = InnateTalent.objects.get(
                category=category, order_id=innate_order
            )
            revealed_quality = QualitiesRevealed.objects.get(
                category=category, order_id=revealed_order
            )
            developed_quality = QualitiesDeveloped.objects.get(
                category=category, order_id=developed_order
            )
        except InnateTalent.DoesNotExist:
            return Response(
                {"error": f"Талант с order_id={innate_order} в InnateTalent не найден"},
                status=HTTP_404_NOT_FOUND,
            )
        except QualitiesRevealed.DoesNotExist:
            return Response(
                {
                    "error": f"Качество с order_id={revealed_order} в QualitiesRevealed не найдено"
                },
                status=HTTP_404_NOT_FOUND,
            )
        except QualitiesDeveloped.DoesNotExist:
            return Response(
                {
                    "error": f"Качество с order_id={developed_order} в QualitiesDeveloped не найдено"
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
                    "innate_talent": InnateTalentSerializer(innate_talent).data,
                    "qualities_revealed": QualitiesRevealedSerializer(
                        revealed_quality
                    ).data,
                    "qualities_developed": QualitiesDevelopedSerializer(
                        developed_quality
                    ).data,
                }
            }
        )
