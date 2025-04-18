from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND
from django.shortcuts import get_object_or_404
from drf_spectacular.utils import extend_schema, OpenApiParameter

from ..models import (
    Category, BirthTalent, 
    YouthTalent, MatureTalent,
    )
from ..serializers.personal_qualities_serializers import (
    CategorySerializer, BirthTalentSerializer, 
    YouthTalentSerializer, MatureTalentSerializer,
)


@extend_schema(tags=['Matrix_Fate'])
class CategoryWithTalentsAPIView(APIView):
    """
    Эндпоинт для получения категории(id=1 или title=Личные качества) + связанные арканы по их order_id.
    """
    serializer_class = CategorySerializer 

    @extend_schema(
        parameters=[
            OpenApiParameter(
                name="birth_a",
                description="Талант при рождении(a)",
                required=True,
                type=int
            ),
            OpenApiParameter(
                name="youth_b",
                description="Талант к 20 годам(b)",
                required=True,
                type=int
            ),
            OpenApiParameter(
                name="mature_c",
                description="Талант к 40 годам(c)",
                required=True,
                type=int
            ),
        ]
    )
    def get(self, request, category_id_or_title):

        if category_id_or_title.isdigit():
            category = get_object_or_404(Category, id=int(category_id_or_title))
        else:
            category = get_object_or_404(Category, title__iexact=category_id_or_title)

        birth_order = request.query_params.get("birth_a")
        youth_order = request.query_params.get("youth_b")
        mature_order = request.query_params.get("mature_c")

        if not (birth_order and youth_order and mature_order):
            return Response(
                {"error": "Необходимо передать три числа (birth, youth, mature)"},
                status=HTTP_400_BAD_REQUEST
            )

        try:
            birth_talent = BirthTalent.objects.get(category=category, order_id=birth_order)
            youth_talent = YouthTalent.objects.get(category=category, order_id=youth_order)
            mature_talent = MatureTalent.objects.get(category=category, order_id=mature_order)
        except BirthTalent.DoesNotExist:
            return Response(
                {"error": f"Талант с order_id={birth_order} в BirthTalent не найден"},
                status=HTTP_404_NOT_FOUND
            )
        except YouthTalent.DoesNotExist:
            return Response(
                {"error": f"Талант с order_id={youth_order} в YouthTalent не найден"},
                status=HTTP_404_NOT_FOUND
            )
        except MatureTalent.DoesNotExist:
            return Response(
                {"error": f"Талант с order_id={mature_order} в MatureTalent не найден"},
                status=HTTP_404_NOT_FOUND
            )

        return Response({
            "category": {
                "id": category.id,
                "title": category.title,
                "description": category.description,
                "is_paid": category.is_paid,
                "birth_talent": BirthTalentSerializer(birth_talent).data,
                "youth_talent": YouthTalentSerializer(youth_talent).data,
                "mature_talent": MatureTalentSerializer(mature_talent).data,
            }
        })