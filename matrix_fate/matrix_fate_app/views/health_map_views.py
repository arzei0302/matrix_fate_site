from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND
from django.shortcuts import get_object_or_404
from drf_spectacular.utils import extend_schema, OpenApiParameter

from common.permissions import IsActivePaidUser


from ..models import (
    Category,
    SahasraraO7,
    SahasraraP7,
    SahasraraQ7,
    AdjnaO6,
    AdjnaP6,
    AdjnaQ6,
    VishudkhaO5,
    VishudkhaP5,
    VishudkhaQ5,
    AnakhataO4,
    AnakhataP4,
    AnakhataQ4,
    ManipuraO3,
    ManipuraP3,
    ManipuraQ3,
    SvadkhistanaO2,
    SvadkhistanaP2,
    SvadkhistanaQ2,
    MuladkharaO1,
    MuladkharaP1,
    MuladkharaQ1,
    TotalO,
    TotalP,
    TotalQ,
)

from ..serializers.health_map_serializers import (
    CategoryWithHealthMapSerializer,
    SahasraraO7Serializer,
    SahasraraP7Serializer,
    SahasraraQ7Serializer,
    AdjnaO6Serializer,
    AdjnaP6Serializer,
    AdjnaQ6Serializer,
    VishudkhaO5Serializer,
    VishudkhaP5Serializer,
    VishudkhaQ5Serializer,
    AnakhataO4Serializer,
    AnakhataP4Serializer,
    AnakhataQ4Serializer,
    ManipuraO3Serializer,
    ManipuraP3Serializer,
    ManipuraQ3Serializer,
    SvadkhistanaO2Serializer,
    SvadkhistanaP2Serializer,
    SvadkhistanaQ2Serializer,
    MuladkharaO1Serializer,
    MuladkharaP1Serializer,
    MuladkharaQ1Serializer,
    TotalOSerializer,
    TotalPSerializer,
    TotalQSerializer,
)


@extend_schema(tags=["Matrix_Fate"])
class CategoryWithHealthMapAPIView(GenericAPIView):
    """Получает категорию по `id(2)` или `title(Карта здоровья)` и арканы по переданным order_id."""

    permission_classes = [IsActivePaidUser]
    serializer_class = CategoryWithHealthMapSerializer

    @extend_schema(
        parameters=[
            OpenApiParameter(
                name="o7", description="Сахасрара O7 (o7)", required=True, type=int
            ),
            OpenApiParameter(
                name="p7", description="Сахасрара P7 (p7)", required=True, type=int
            ),
            OpenApiParameter(
                name="q7", description="Сахасрара Q7 (q7)", required=True, type=int
            ),
            OpenApiParameter(
                name="o6", description="Аджна O6 (o6)", required=True, type=int
            ),
            OpenApiParameter(
                name="p6", description="Аджна P6 (p6)", required=True, type=int
            ),
            OpenApiParameter(
                name="q6", description="Аджна Q6 (q6)", required=True, type=int
            ),
            OpenApiParameter(
                name="o5", description="Вишудха O5 (o5)", required=True, type=int
            ),
            OpenApiParameter(
                name="p5", description="Вишудха P5 (p5)", required=True, type=int
            ),
            OpenApiParameter(
                name="q5", description="Вишудха Q5 (q5)", required=True, type=int
            ),
            OpenApiParameter(
                name="o4", description="Анахата O4 (o4)", required=True, type=int
            ),
            OpenApiParameter(
                name="p4", description="Анахата P4 (p4)", required=True, type=int
            ),
            OpenApiParameter(
                name="q4", description="Анахата Q4 (q4)", required=True, type=int
            ),
            OpenApiParameter(
                name="o3", description="Манипура O3 (o3)", required=True, type=int
            ),
            OpenApiParameter(
                name="p3", description="Манипура P3 (p3)", required=True, type=int
            ),
            OpenApiParameter(
                name="q3", description="Манипура Q3 (q3)", required=True, type=int
            ),
            OpenApiParameter(
                name="o2", description="Свадхистана O2 (o2)", required=True, type=int
            ),
            OpenApiParameter(
                name="p2", description="Свадхистана P2 (p2)", required=True, type=int
            ),
            OpenApiParameter(
                name="q2", description="Свадхистана Q2 (q2)", required=True, type=int
            ),
            OpenApiParameter(
                name="o1", description="Муладхара O1 (o1)", required=True, type=int
            ),
            OpenApiParameter(
                name="p1", description="Муладхара P1 (p1)", required=True, type=int
            ),
            OpenApiParameter(
                name="q1", description="Муладхара Q1 (q1)", required=True, type=int
            ),
            OpenApiParameter(
                name="o", description="Итого O (o)", required=True, type=int
            ),
            OpenApiParameter(
                name="p", description="Итого P (p)", required=True, type=int
            ),
            OpenApiParameter(
                name="q", description="Итого Q (q)", required=True, type=int
            ),
        ]
    )
    def get(self, request, category_id_or_title):

        if category_id_or_title.isdigit():
            category = get_object_or_404(Category, id=int(category_id_or_title))
        else:
            category = get_object_or_404(Category, title__iexact=category_id_or_title)

        order_params = {
            "o7": (SahasraraO7, SahasraraO7Serializer),
            "p7": (SahasraraP7, SahasraraP7Serializer),
            "q7": (SahasraraQ7, SahasraraQ7Serializer),
            "o6": (AdjnaO6, AdjnaO6Serializer),
            "p6": (AdjnaP6, AdjnaP6Serializer),
            "q6": (AdjnaQ6, AdjnaQ6Serializer),
            "o5": (VishudkhaO5, VishudkhaO5Serializer),
            "p5": (VishudkhaP5, VishudkhaP5Serializer),
            "q5": (VishudkhaQ5, VishudkhaQ5Serializer),
            "o4": (AnakhataO4, AnakhataO4Serializer),
            "p4": (AnakhataP4, AnakhataP4Serializer),
            "q4": (AnakhataQ4, AnakhataQ4Serializer),
            "o3": (ManipuraO3, ManipuraO3Serializer),
            "p3": (ManipuraP3, ManipuraP3Serializer),
            "q3": (ManipuraQ3, ManipuraQ3Serializer),
            "o2": (SvadkhistanaO2, SvadkhistanaO2Serializer),
            "p2": (SvadkhistanaP2, SvadkhistanaP2Serializer),
            "q2": (SvadkhistanaQ2, SvadkhistanaQ2Serializer),
            "o1": (MuladkharaO1, MuladkharaO1Serializer),
            "p1": (MuladkharaP1, MuladkharaP1Serializer),
            "q1": (MuladkharaQ1, MuladkharaQ1Serializer),
            "o": (TotalO, TotalOSerializer),
            "p": (TotalP, TotalPSerializer),
            "q": (TotalQ, TotalQSerializer),
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
