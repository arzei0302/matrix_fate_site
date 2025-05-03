from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND
from django.shortcuts import get_object_or_404
from drf_spectacular.utils import extend_schema, OpenApiParameter

from matrix_fate.common.permissions import is_active_paid_user

# from matrix_fate.common.permissions import IsActivePaidUser

from ..models import Category, SoulMainTask, PastLifeExperience, PastLifeLesson
from ..serializers.past_life_task_serializers import (
    CategoryPastLifeTaskSerializer,
    SoulMainTaskSerializer,
    PastLifeExperienceSerializer,
    PastLifeLessonSerializer,
)


@extend_schema(tags=["Matrix_Fate"])
class CategoryWithPastLifeTaskAPIView(APIView):
    """Получает категорию(id=9) или title(Задачи которые тянутся из прошлых жизней) и таланты по переданным `order_id`."""

    # permission_classes = [IsActivePaidUser]
    serializer_class = CategoryPastLifeTaskSerializer

    @extend_schema(
        parameters=[
            OpenApiParameter(
                name="main",
                description="Главная задача Души (d)",
                required=True,
                type=int,
            ),
            OpenApiParameter(
                name="experience",
                description="Опыт вашей души в прошлом с людьми (d2)",
                required=True,
                type=int,
            ),
            OpenApiParameter(
                name="lesson",
                description="Урок из прошлой жизни (d1)",
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

        main_order = request.query_params.get("main")
        experience_order = request.query_params.get("experience")
        lesson_order = request.query_params.get("lesson")

        if not (main_order and experience_order and lesson_order):
            return Response(
                {"error": "Необходимо передать три числа (main, experience, lesson)"},
                status=HTTP_400_BAD_REQUEST,
            )

        try:
            main_task = SoulMainTask.objects.get(category=category, order_id=main_order)
            experience = PastLifeExperience.objects.get(
                category=category, order_id=experience_order
            )
            lesson = PastLifeLesson.objects.get(
                category=category, order_id=lesson_order
            )
        except SoulMainTask.DoesNotExist:
            return Response(
                {"error": f"Задача с order_id={main_order} в SoulMainTask не найдена"},
                status=HTTP_404_NOT_FOUND,
            )
        except PastLifeExperience.DoesNotExist:
            return Response(
                {
                    "error": f"Опыт с order_id={experience_order} в PastLifeExperience не найден"
                },
                status=HTTP_404_NOT_FOUND,
            )
        except PastLifeLesson.DoesNotExist:
            return Response(
                {"error": f"Урок с order_id={lesson_order} в PastLifeLesson не найден"},
                status=HTTP_404_NOT_FOUND,
            )

        return Response(
            {
                "category": {
                    "id": category.id,
                    "title": category.title,
                    "description": category.description,
                    "is_paid": category.is_paid,
                    "soul_main_task": SoulMainTaskSerializer(main_task).data,
                    "past_life_experience": PastLifeExperienceSerializer(
                        experience
                    ).data,
                    "past_life_lesson": PastLifeLessonSerializer(lesson).data,
                }
            }
        )
