from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND
from django.shortcuts import get_object_or_404
from drf_spectacular.utils import extend_schema, OpenApiParameter

from common.permissions import IsActivePaidUser

from ..models import (
    Category,
    PaternalDiseases,
    MaternalDiseases,
    HealthArcane1,
    HealthArcane2,
    HealthArcane3,
)
from ..serializers.disease_predisposition_serializers import (
    CategoryWithDiseasePredispositionSerializer,
    PaternalDiseasesSerializer,
    MaternalDiseasesSerializer,
    HealthArcane1Serializer,
    HealthArcane2Serializer,
    HealthArcane3Serializer,
)


@extend_schema(tags=["Matrix_Fate"])
class CategoryWithDiseasePredispositionAPIView(GenericAPIView):
    """Получает категорию по `id(17)` или `title(Предрасположенность к заболеваниям)` и арканы по переданным order_id."""

    permission_classes = [IsActivePaidUser]
    serializer_class = (CategoryWithDiseasePredispositionSerializer)

    @extend_schema(
        parameters=[
            OpenApiParameter(
                name="paternal",
                description="Родовые заболевания по линии отца (h)",
                required=True,
                type=int,
            ),
            OpenApiParameter(
                name="maternal",
                description="Родовые заболевания по линии матери (i)",
                required=True,
                type=int,
            ),
            OpenApiParameter(
                name="a1", description="Аркан1 (a)", required=True, type=int
            ),
            OpenApiParameter(
                name="a2", description="Аркан2 (b)", required=True, type=int
            ),
            OpenApiParameter(
                name="a3", description="Аркан3 (c)", required=True, type=int
            ),
        ]
    )
    def get(self, request, category_id_or_title):

        if category_id_or_title.isdigit():
            category = get_object_or_404(Category, id=int(category_id_or_title))
        else:
            category = get_object_or_404(Category, title__iexact=category_id_or_title)

        order_params = {
            "paternal": (PaternalDiseases, PaternalDiseasesSerializer),
            "maternal": (MaternalDiseases, MaternalDiseasesSerializer),
            "a1": (HealthArcane1, HealthArcane1Serializer),
            "a2": (HealthArcane2, HealthArcane2Serializer),
            "a3": (HealthArcane3, HealthArcane3Serializer),
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
                response_data[param] = serializer_class(
                    instance
                ).data  # ✅ Используем сериализатор
            except model.DoesNotExist:
                return Response(
                    {"error": f"{param} с order_id={order_id} не найден"},
                    status=HTTP_404_NOT_FOUND,
                )

        return Response(response_data)
