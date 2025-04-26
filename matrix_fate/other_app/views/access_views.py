from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from drf_spectacular.utils import extend_schema

from matrix_fate.other_app.serializers.access_serializers import AccessMatrixSerializer

from ..models import AccessMatrixModel

@extend_schema(tags=['Access'])
class AccessMatrixListView(generics.ListAPIView):
    """
    Получение всех активных тарифных планов (GET /api/tariffs/)
    """
    queryset = AccessMatrixModel.objects.filter(is_active=True).order_by('order')
    serializer_class = AccessMatrixSerializer
    permission_classes = [AllowAny]


@extend_schema(tags=['Access'])

class AccessMatrixDetailView(generics.RetrieveAPIView):
    """
    Получение тарифа по его ID (GET /api/tariffs/<id>/)
    """
    queryset = AccessMatrixModel.objects.filter(is_active=True)
    serializer_class = AccessMatrixSerializer
    permission_classes = [AllowAny]
    lookup_field = 'id'
