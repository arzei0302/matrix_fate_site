from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND
from django.shortcuts import get_object_or_404
from drf_spectacular.utils import extend_schema, OpenApiParameter

from matrix_fate.common.permissions import is_active_paid_user

# from matrix_fate.common.permissions import IsActivePaidUser

from ..models import (
    Category,
    PartnerTasks,
    SuitablePartner,
    MeetingPlace,
    RelationshipProblems,
)
from ..serializers.matrix_relationships_serializers import (
    CategoryWithMatrixRelationshipsSerializer,
    PartnerTasksSerializer,
    SuitablePartnerSerializer,
    MeetingPlaceSerializer,
    RelationshipProblemsSerializer,
)
from matrix_fate.common.mixins import PaidCategoryAccessMixin


@extend_schema(tags=["Matrix_Fate"])
class CategoryWithMatrixRelationshipsAPIView(APIView, PaidCategoryAccessMixin):
    """Получает категорию по `id(14)` или `title(Отношения в матрице)` и информацию о партнерских отношениях по переданным order_id."""

    # permission_classes = [IsActivePaidUser]
    serializer_class = CategoryWithMatrixRelationshipsSerializer

    @extend_schema(
        parameters=[
            OpenApiParameter(
                name="tasks",
                description="Какие задачи стоят с партнерами (d2)",
                required=True,
                type=int,
            ),
            OpenApiParameter(
                name="partner",
                description="Какой партнер вам подходит (k)",
                required=True,
                type=int,
            ),
            OpenApiParameter(
                name="meeting",
                description="Где можете познакомиться с партнером (k)",
                required=True,
                type=int,
            ),
            OpenApiParameter(
                name="problems",
                description="Какие могут возникнуть проблемы в отношениях (j)",
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

        tasks_order = request.query_params.get("tasks")
        partner_order = request.query_params.get("partner")
        meeting_order = request.query_params.get("meeting")
        problems_order = request.query_params.get("problems")

        if not (tasks_order and partner_order and meeting_order and problems_order):
            return Response(
                {
                    "error": "Необходимо передать четыре числа (tasks, partner, meeting, problems)"
                },
                status=HTTP_400_BAD_REQUEST,
            )

        try:
            partner_tasks = PartnerTasks.objects.get(
                category=category, order_id=tasks_order
            )
            suitable_partner = SuitablePartner.objects.get(
                category=category, order_id=partner_order
            )
            meeting_place = MeetingPlace.objects.get(
                category=category, order_id=meeting_order
            )
            relationship_problems = RelationshipProblems.objects.get(
                category=category, order_id=problems_order
            )
        except PartnerTasks.DoesNotExist:
            return Response(
                {"error": f"Задача с order_id={tasks_order} в PartnerTasks не найдена"},
                status=HTTP_404_NOT_FOUND,
            )
        except SuitablePartner.DoesNotExist:
            return Response(
                {
                    "error": f"Партнер с order_id={partner_order} в SuitablePartner не найден"
                },
                status=HTTP_404_NOT_FOUND,
            )
        except MeetingPlace.DoesNotExist:
            return Response(
                {
                    "error": f"Место знакомства с order_id={meeting_order} в MeetingPlace не найдено"
                },
                status=HTTP_404_NOT_FOUND,
            )
        except RelationshipProblems.DoesNotExist:
            return Response(
                {
                    "error": f"Проблема с order_id={problems_order} в RelationshipProblems не найдена"
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
                    "partner_tasks": PartnerTasksSerializer(partner_tasks).data,
                    "suitable_partner": SuitablePartnerSerializer(
                        suitable_partner
                    ).data,
                    "meeting_place": MeetingPlaceSerializer(meeting_place).data,
                    "relationship_problems": RelationshipProblemsSerializer(
                        relationship_problems
                    ).data,
                }
            }
        )
