from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND
from django.shortcuts import get_object_or_404
from drf_spectacular.utils import extend_schema, OpenApiParameter

from matrix_fate.common.permissions import IsActivePaidUser

from ..models import (
    Category,
    PersonalPurpose1,
    PersonalPurpose2,
    PersonalPurpose3,
    SocialPurpose1,
    SocialPurpose2,
    SocialPurpose3,
    SpiritualPurpose,
)
from ..serializers.soul_mission_serializers import (
    CategoryWithSoulMissionSerializer,
    PersonalPurpose1Serializer,
    PersonalPurpose2Serializer,
    PersonalPurpose3Serializer,
    SocialPurpose1Serializer,
    SocialPurpose2Serializer,
    SocialPurpose3Serializer,
    SpiritualPurposeSerializer,
)


@extend_schema(tags=["Matrix_Fate"])
class CategoryWithSoulMissionAPIView(GenericAPIView):
    """Получает категорию по `id(16)` или `title(Предназначение)` и информацию о предназначении по переданным order_id."""

    permission_classes = [IsActivePaidUser]
    serializer_class = CategoryWithSoulMissionSerializer

    @extend_schema(
        parameters=[
            OpenApiParameter(
                name="p1",
                description="Задача для персонального 1 Аркана (r)",
                required=True,
                type=int,
            ),
            OpenApiParameter(
                name="p2",
                description="Задача для персонального 2 Аркана (s)",
                required=True,
                type=int,
            ),
            OpenApiParameter(
                name="p3",
                description="Задача для персонального 3 Аркана (y)",
                required=True,
                type=int,
            ),
            OpenApiParameter(
                name="s1",
                description="Задача для социального 1 Аркана (t)",
                required=True,
                type=int,
            ),
            OpenApiParameter(
                name="s2",
                description="Задача для социального 2 Аркана (u)",
                required=True,
                type=int,
            ),
            OpenApiParameter(
                name="s3",
                description="Задача для социального 3 Аркана (v)",
                required=True,
                type=int,
            ),
            OpenApiParameter(
                name="spiritual",
                description="Духовное предназначение (w)",
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

        order_params = {
            "p1": (PersonalPurpose1, PersonalPurpose1Serializer),
            "p2": (PersonalPurpose2, PersonalPurpose2Serializer),
            "p3": (PersonalPurpose3, PersonalPurpose3Serializer),
            "s1": (SocialPurpose1, SocialPurpose1Serializer),
            "s2": (SocialPurpose2, SocialPurpose2Serializer),
            "s3": (SocialPurpose3, SocialPurpose3Serializer),
            "spiritual": (SpiritualPurpose, SpiritualPurposeSerializer),
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
