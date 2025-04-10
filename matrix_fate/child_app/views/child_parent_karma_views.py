from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND
from django.shortcuts import get_object_or_404
from drf_spectacular.utils import extend_schema, OpenApiParameter

from ..models import (
    ChildCategory,
    WhatChildShouldTeachParents,
    WhatMistakesRelationshipParentsChildren,
    WhatShouldComeQualitiesChild,
)
from ..serializers.child_parent_karma_serializers import (
    WhatChildShouldTeachParentsSerializer,
    WhatMistakesRelationshipParentsChildrenSerializer,
    WhatShouldComeQualitiesChildSerializer,
    ChildCategoryParentKarmaSerializer
)

@extend_schema(tags=["Child Matrix"])
class ChildCategoryWithParentKarmaAPIView(APIView):
    """
    Эндпоинт для получения категории (id=7 или title=Детско-родительская карма) + связанные арканы по order_id.
    """

    serializer_class = ChildCategoryParentKarmaSerializer

    @extend_schema(
        parameters=[
            OpenApiParameter(name="arcana_a", description="Аркан (a) - Чему ребенок должен научить родителей", required=False, type=int),
            OpenApiParameter(name="arcana_a2", description="Аркан (a2) - Ошибки во взаимоотношениях", required=False, type=int),
            OpenApiParameter(name="arcana_a1", description="Аркан (a1) - К чему должен прийти ребенок", required=False, type=int),
        ]
    )
    def get(self, request, category_id_or_title):

        if category_id_or_title.isdigit():
            category = get_object_or_404(ChildCategory, id=int(category_id_or_title))
        else:
            category = get_object_or_404(ChildCategory, title__iexact=category_id_or_title)

        arcana_a_order = request.query_params.get("arcana_a")
        arcana_a2_order = request.query_params.get("arcana_a2")
        arcana_a1_order = request.query_params.get("arcana_a1")

        response_data = {
            "id": category.id,
            "title": category.title,
            "description": category.description,
            "is_paid": category.is_paid,
        }

        if arcana_a_order:
            try:
                arcana_a = WhatChildShouldTeachParents.objects.get(category=category, order_id=arcana_a_order)
                response_data["arcana_a"] = WhatChildShouldTeachParentsSerializer(arcana_a).data
            except WhatChildShouldTeachParents.DoesNotExist:
                return Response(
                    {"error": f"Аркан с order_id={arcana_a_order} в WhatChildShouldTeachParents не найден"},
                    status=HTTP_404_NOT_FOUND,
                )

        if arcana_a2_order:
            try:
                arcana_a2 = WhatMistakesRelationshipParentsChildren.objects.get(category=category, order_id=arcana_a2_order)
                response_data["arcana_a2"] = WhatMistakesRelationshipParentsChildrenSerializer(arcana_a2).data
            except WhatMistakesRelationshipParentsChildren.DoesNotExist:
                return Response(
                    {"error": f"Аркан с order_id={arcana_a2_order} в WhatMistakesRelationshipParentsChildren не найден"},
                    status=HTTP_404_NOT_FOUND,
                )

        if arcana_a1_order:
            try:
                arcana_a1 = WhatShouldComeQualitiesChild.objects.get(category=category, order_id=arcana_a1_order)
                response_data["arcana_a1"] = WhatShouldComeQualitiesChildSerializer(arcana_a1).data
            except WhatShouldComeQualitiesChild.DoesNotExist:
                return Response(
                    {"error": f"Аркан с order_id={arcana_a1_order} в WhatShouldComeQualitiesChild не найден"},
                    status=HTTP_404_NOT_FOUND,
                )

        if not arcana_a_order and not arcana_a2_order and not arcana_a1_order:
            return Response(
                {"error": "Необходимо передать хотя бы один order_id аркана (arcana_a, arcana_a2, arcana_a1)"},
                status=HTTP_400_BAD_REQUEST,
            )

        return Response({"category": response_data})
