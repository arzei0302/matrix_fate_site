from rest_framework.response import Response
from rest_framework.views import APIView
from drf_spectacular.utils import extend_schema, OpenApiExample, OpenApiParameter
import random
from ..serializers.fin_and_anti_code_serializer import FinancialAndAntiCodeCalculationSerializer
from ..models import FinancialAndAntiCodeCalculation
from matrix_fate.compatibility_app.service.calculator_matrix_compatibility_view import reduce_to_22
from rest_framework import status


# @extend_schema(
#     tags=['Additional Calc'],
#     responses={200: FinancialAndAntiCodeCalculationSerializer(many=True)},
#     examples=[
#         OpenApiExample(
#             name="Рассчет финкода и антикода",
#             description="Рассчет финкода и антикода",
#             value={"past": "Рассчет финкода и антикода"}
#         )
#     ]
# )
# class FinancialAndAntiCodeCalculationView(APIView):
#     """Рассчитать финкод и антикод"""
#     serializer_class = FinancialAndAntiCodeCalculationSerializer

#     def get(self, request):
#         code = random.choice(FinancialAndAntiCodeCalculation.objects.all())
#         serializer = self.serializer_class(code)
#         return Response(serializer.data)




from datetime import datetime

class FinancialAndAntiCodeByBirthDateView(APIView):
    """Получить финкод и антикод по дате рождения"""

    serializer_class = FinancialAndAntiCodeCalculationSerializer

    @extend_schema(
        tags=['Additional Calc'],
        parameters=[
            OpenApiParameter(
                name='birth_date',
                description='Дата рождения в формате ДД.ММ.ГГГГ',
                required=True,
                type=str,
                location=OpenApiParameter.QUERY
            )
        ],
        responses={200: FinancialAndAntiCodeCalculationSerializer},
        examples=[
            OpenApiExample(
                name="Пример запроса",
                description="Пример: /api/fincode-by-birth?birth_date=12-05-1990",
                value={"birth_date": "12-05-1990"}
            )
        ]
    )
    def get(self, request):
        birth_date_str = request.query_params.get('birth_date')
        if not birth_date_str:
            return Response({'error': 'birth_date параметр обязателен'}, status=status.HTTP_400_BAD_REQUEST)
    
        try:
            birth_date = datetime.strptime(birth_date_str, '%d.%m.%Y').date()
        except ValueError:
            return Response({'error': 'birth_date должен быть в формате ДД.ММ.ГГГГ, например: 1.1.2025'}, status=status.HTTP_400_BAD_REQUEST)
    
        date_number = int(birth_date.strftime('%Y%m%d'))
        reduced_id = reduce_to_22(date_number)
    
        try:
            code = FinancialAndAntiCodeCalculation.objects.get(id=reduced_id)
        except FinancialAndAntiCodeCalculation.DoesNotExist:
            return Response({'error': f'Запись с id={reduced_id} не найдена'}, status=status.HTTP_404_NOT_FOUND)
    
        serializer = self.serializer_class(code)
        return Response(serializer.data)

