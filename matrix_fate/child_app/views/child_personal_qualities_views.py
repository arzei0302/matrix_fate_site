from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND
from django.shortcuts import get_object_or_404
from drf_spectacular.utils import extend_schema, OpenApiParameter

from matrix_fate.common.permissions import is_active_paid_user

from ..models import ChildCategory, QualitiesRevealedAgeOf20, ThirdTalentRevealedAge40
from ..serializers.child_personal_qualities_serializers import (
    ChildCategoryPersonalQualitiesSerializer,
    QualitiesRevealedAgeOf20Serializer,
    ThirdTalentRevealedAge40Serializer,
)
from matrix_fate.common.mixins import PaidCategoryAccessMixin



@extend_schema(tags=["Child Matrix"])
class ChildCategoryWithPersonalQualitiesAPIView(APIView, PaidCategoryAccessMixin):
    """
    Эндпоинт для получения категории (id=2 или title=Личные качества) + связанный аркан по order_id.
    """
    # permission_classes = [IsActivePaidUser]
    serializer_class = ChildCategoryPersonalQualitiesSerializer

    @extend_schema(
        parameters=[
            OpenApiParameter(
                name="arcana_b", description="Аркан (b)", required=False, type=int
            ),
            OpenApiParameter(
                name="arcana_c", description="Аркан (c)", required=False, type=int
            ),
        ]
    )
    def get(self, request, category_id_or_title):

        if category_id_or_title.isdigit():
            category = get_object_or_404(
                ChildCategory, id=int(category_id_or_title)
            )
        else:
            category = get_object_or_404(
                ChildCategory, title__iexact=category_id_or_title
            )

        access_response = self.check_category_access(request, category)
        if access_response:
            return access_response

        arcana_b_order = request.query_params.get("arcana_b")
        arcana_c_order = request.query_params.get("arcana_c")

        response_data = {
            "id": category.id,
            "title": category.title,
            "description": category.description,
            "is_paid": category.is_paid,
        }

        if arcana_b_order:
            try:
                arcana_b = QualitiesRevealedAgeOf20.objects.get(category=category, order_id=arcana_b_order)
                response_data["arcana_b"] = QualitiesRevealedAgeOf20Serializer(arcana_b).data
            except QualitiesRevealedAgeOf20.DoesNotExist:
                return Response(
                    {"error": f"Аркан с order_id={arcana_b_order} в QualitiesRevealedAgeOf20 не найден"},
                    status=HTTP_404_NOT_FOUND,
                )

        if arcana_c_order:
            try:
                arcana_c = ThirdTalentRevealedAge40.objects.get(category=category, order_id=arcana_c_order)
                response_data["arcana_c"] = ThirdTalentRevealedAge40Serializer(arcana_c).data
            except ThirdTalentRevealedAge40.DoesNotExist:
                return Response(
                    {"error": f"Аркан с order_id={arcana_c_order} в ThirdTalentRevealedAge40 не найден"},
                    status=HTTP_404_NOT_FOUND,
                )

        if not arcana_b_order and not arcana_c_order:
            return Response(
                {"error": "Необходимо передать хотя бы один order_id аркана (arcana_b или arcana_c)"},
                status=HTTP_400_BAD_REQUEST,
            )

        return Response({"category": response_data})
