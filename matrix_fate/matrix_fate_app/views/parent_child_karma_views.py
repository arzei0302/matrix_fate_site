from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND
from django.shortcuts import get_object_or_404
from drf_spectacular.utils import extend_schema, OpenApiParameter

from matrix_fate.common.permissions import is_active_paid_user

# from matrix_fate.common.permissions import IsActivePaidUser

from ..models import Category, TeachParents, RelationshipMistakes, PersonalGrowth
from ..serializers.parent_child_karma_serializers import (
    CategoryWithParentChildKarmaSerializer,
    TeachParentsSerializer,
    RelationshipMistakesSerializer,
    PersonalGrowthSerializer,
)
from matrix_fate.common.mixins import PaidCategoryAccessMixin


@extend_schema(tags=["Matrix_Fate"])
class CategoryWithParentChildKarmaAPIView(APIView, PaidCategoryAccessMixin):
    """Получает категорию по `id(12)` или `title(Детско-родительская карма)` и три аспекта детско-родительской кармы по переданным order_id."""
    
    # permission_classes = [IsActivePaidUser]
    serializer_class = CategoryWithParentChildKarmaSerializer

    @extend_schema(
        parameters=[
            OpenApiParameter(
                name="teach",
                description="Чему вы должны были научить родителей (a)",
                required=True,
                type=int,
            ),
            OpenApiParameter(
                name="mistakes",
                description="Ошибки в отношениях с родителями и детьми (a2)",
                required=True,
                type=int,
            ),
            OpenApiParameter(
                name="growth",
                description="К чему должны прийти, какие качества необходимо в себе наработать (a1)",
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

        access_response = self.check_category_access(request, category)
        if access_response:
            return access_response

        teach_order = request.query_params.get("teach")
        mistakes_order = request.query_params.get("mistakes")
        growth_order = request.query_params.get("growth")

        if not (teach_order and mistakes_order and growth_order):
            return Response(
                {"error": "Необходимо передать три числа (teach, mistakes, growth)"},
                status=HTTP_400_BAD_REQUEST,
            )

        try:
            teach_parents = TeachParents.objects.get(
                category=category, order_id=teach_order
            )
            relationship_mistakes = RelationshipMistakes.objects.get(
                category=category, order_id=mistakes_order
            )
            personal_growth = PersonalGrowth.objects.get(
                category=category, order_id=growth_order
            )
        except TeachParents.DoesNotExist:
            return Response(
                {"error": f"Запись с order_id={teach_order} в TeachParents не найдена"},
                status=HTTP_404_NOT_FOUND,
            )
        except RelationshipMistakes.DoesNotExist:
            return Response(
                {
                    "error": f"Запись с order_id={mistakes_order} в RelationshipMistakes не найдена"
                },
                status=HTTP_404_NOT_FOUND,
            )
        except PersonalGrowth.DoesNotExist:
            return Response(
                {
                    "error": f"Запись с order_id={growth_order} в PersonalGrowth не найдена"
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
                    "teach_parents": TeachParentsSerializer(teach_parents).data,
                    "relationship_mistakes": RelationshipMistakesSerializer(
                        relationship_mistakes
                    ).data,
                    "personal_growth": PersonalGrowthSerializer(personal_growth).data,
                }
            }
        )
