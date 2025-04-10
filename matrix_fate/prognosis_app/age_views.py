from drf_spectacular.utils import extend_schema, OpenApiParameter
from rest_framework.pagination import PageNumberPagination
from rest_framework import generics

from common.permissions import IsActivePaidUser
from .models import BreakdownByYear
from .age_serializers import BreakdownByYearSerializer


class BreakdownByYearPagination(PageNumberPagination):
    page_size = 1
    page_size_query_param = 'page_size'
    max_page_size = 1


# @extend_schema(
#     tags=["Matrix Age"],
#     parameters=[
#         OpenApiParameter(name="page", description="Номер страницы", required=False, type=int),
#         OpenApiParameter(name="page_size", description="Количество объектов на страницу (максимум 1)", required=False, type=int),
#     ]
# )
# class BreakdownByYearListView(generics.ListAPIView):
#     """Разбор по годам"""
#     queryset = BreakdownByYear.objects.all().order_by('id')
#     serializer_class = BreakdownByYearSerializer
#     pagination_class = BreakdownByYearPagination

from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiExample

@extend_schema(
    tags=["Matrix Age"],
    parameters=[
        OpenApiParameter(
            name="page",
            description="Номер страницы (по умолчанию 1)",
            required=False,
            type=int,
            examples=[
                OpenApiExample(
                    name="Пример страницы",
                    value=1,
                    summary="Первая страница"
                )
            ]
        ),
        OpenApiParameter(
            name="page_size",
            description="Количество объектов на страницу (фиксировано: 1)",
            required=False,
            type=int,
            examples=[
                OpenApiExample(
                    name="Один объект",
                    value=1,
                    summary="1 объект на страницу"
                )
            ]
        ),
    ]
)
class BreakdownByYearListView(generics.ListAPIView):
    """Разбор по годам"""

    permission_classes = [IsActivePaidUser]

    queryset = BreakdownByYear.objects.all().order_by('id')
    serializer_class = BreakdownByYearSerializer
    pagination_class = BreakdownByYearPagination


