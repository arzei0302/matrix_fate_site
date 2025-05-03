from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND
from django.shortcuts import get_object_or_404
from drf_spectacular.utils import extend_schema, OpenApiParameter

from matrix_fate.common.permissions import is_active_paid_user

# from matrix_fate.common.permissions import IsActivePaidUser

from ..models import (
    Category,
    AncestralTaskFatherMale,
    AncestralTaskMotherMale,
    AncestralTaskFatherFemale,
    AncestralTaskMotherFemale,
)
from ..serializers.ancestral_task7_serializers import (
    CategoryWithAncestralTask7Serializer,
    AncestralTaskFatherMaleSerializer,
    AncestralTaskMotherMaleSerializer,
    AncestralTaskFatherFemaleSerializer,
    AncestralTaskMotherFemaleSerializer,
)


@extend_schema(tags=["Matrix_Fate"])
class CategoryWithAncestralTask7APIView(GenericAPIView):
    """Получает категорию по `id(18)` или `title(Задачи рода до 7 колена)` и информацию о задачах рода по переданным order_id."""

    # permission_classes = [IsActivePaidUser]
    serializer_class = CategoryWithAncestralTask7Serializer

    @extend_schema(
        parameters=[
            OpenApiParameter(
                name="fm",
                description="Задачи по мужской линии по роду отца (f)",
                required=True,
                type=int,
            ),
            OpenApiParameter(
                name="mm",
                description="Задачи по мужской линии по роду матери (h)",
                required=True,
                type=int,
            ),
            OpenApiParameter(
                name="ff",
                description="Задачи по женской линии по роду отца (g)",
                required=True,
                type=int,
            ),
            OpenApiParameter(
                name="mf",
                description="Задачи по женской линии по роду матери (i)",
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

        if not is_active_paid_user(request.user):
            return Response({
                "category": {
                    "id": category.id,
                    "title": category.title,
                }
            })

        order_params = {
            "fm": (AncestralTaskFatherMale, AncestralTaskFatherMaleSerializer),
            "mm": (AncestralTaskMotherMale, AncestralTaskMotherMaleSerializer),
            "ff": (AncestralTaskFatherFemale, AncestralTaskFatherFemaleSerializer),
            "mf": (AncestralTaskMotherFemale, AncestralTaskMotherFemaleSerializer),
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
