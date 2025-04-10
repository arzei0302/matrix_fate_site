from rest_framework.decorators import api_view
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema
from rest_framework import serializers
import logging

from common.input_data import normalize_input_data
from matrix_auth_app.models import UserCalculationHistory

from .calculator_compatibility_serializer import MatrixCompability2InputSerializer, MatrixCompability2OutputSerializer
from .calculator_matrix_compatibility_view import reduce_to_22

logger = logging.getLogger(__name__)

class ErrorSerializer(serializers.Serializer):
    error = serializers.CharField()

@extend_schema(
    tags=['Compatibility Matrix'],
    request=MatrixCompability2InputSerializer,
    responses={200: MatrixCompability2OutputSerializer, 400: ErrorSerializer},
)


@api_view(["POST"])
def calculate_compatibility_view(request):
    serializer = MatrixCompability2InputSerializer(data=request.data)
    if not serializer.is_valid():
        return Response(serializer.errors, status=400)

    birth_day = serializer.validated_data["day"]
    birth_month = serializer.validated_data["month"]
    birth_year = serializer.validated_data["year"]

    birth_day2 = serializer.validated_data["day2"]
    birth_month2 = serializer.validated_data["month2"]
    birth_year2 = serializer.validated_data["year2"]

    if not (1 <= birth_month <= 12) or not (1 <= birth_month2 <= 12):
        return Response({"error": "Месяц должен быть в диапазоне 1-12"}, status=400)


# значения из matrix_fate - 1
    schem_1_a = reduce_to_22(birth_day)
    schem_1_b = reduce_to_22(birth_month)
    schem_1_c = reduce_to_22(birth_year)
    schem_1_d = reduce_to_22(schem_1_a + schem_1_b + schem_1_c)
    schem_1_e = reduce_to_22(schem_1_a + schem_1_b + schem_1_c + schem_1_d)
    schem_1_f = reduce_to_22(schem_1_a + schem_1_b)
    schem_1_g = reduce_to_22(schem_1_b + schem_1_c)
    schem_1_h = reduce_to_22(schem_1_c + schem_1_d)
    schem_1_i = reduce_to_22(schem_1_d + schem_1_a)
    
# значения из matrix_fate - 2
    schem_2_a = reduce_to_22(birth_day2)
    schem_2_b = reduce_to_22(birth_month2)
    schem_2_c = reduce_to_22(birth_year2)
    schem_2_d = reduce_to_22(schem_2_a + schem_2_b + schem_2_c)
    schem_2_e = reduce_to_22(schem_2_a + schem_2_b + schem_2_c + schem_2_d)
    schem_2_f = reduce_to_22(schem_2_a + schem_2_b)
    schem_2_g = reduce_to_22(schem_2_b + schem_2_c)
    schem_2_h = reduce_to_22(schem_2_c + schem_2_d)
    schem_2_i = reduce_to_22(schem_2_d + schem_2_a)

#  объединенные значения 
    a = reduce_to_22(reduce_to_22(schem_1_a) + reduce_to_22(schem_2_a))
    b = reduce_to_22(reduce_to_22(schem_1_b) + reduce_to_22(schem_2_b))
    c = reduce_to_22(reduce_to_22(schem_1_c) + reduce_to_22(schem_2_c))
    d = reduce_to_22(reduce_to_22(schem_1_d) + reduce_to_22(schem_2_d))
    e = reduce_to_22(reduce_to_22(schem_1_e) + reduce_to_22(schem_2_e))
    f = reduce_to_22(reduce_to_22(schem_1_f) + reduce_to_22(schem_2_f))
    g = reduce_to_22(reduce_to_22(schem_1_g) + reduce_to_22(schem_2_g))
    h = reduce_to_22(reduce_to_22(schem_1_h) + reduce_to_22(schem_2_h))
    i = reduce_to_22(reduce_to_22(schem_1_i) + reduce_to_22(schem_2_i))

    d2 = reduce_to_22(d + e)
    d1 = reduce_to_22(d + d2)
    c2 = reduce_to_22(c + e)

    j = reduce_to_22(d2 + c2)
    k = reduce_to_22(d2 + j)
    l = reduce_to_22(c2 + j)

    r = reduce_to_22(b + d)
    s = reduce_to_22(c + a)
    y = reduce_to_22(r + s)

    t = reduce_to_22(f + h)
    u = reduce_to_22(g + i)
    v = reduce_to_22(t + u)

    w = reduce_to_22(y + v)
    

    compatibility_matrix_value = {
        "category": "compatibility",
        "a": a,
        "b": b,
        "c": c,
        "d": d,
        "e": e,
        "f": f,
        "g": g,
        "h": h,
        "i": i,
        
        "d2": d2,
        "d1": d1,
        "c2": c2,

        "j": j,
        "k": k,
        "l": l,

        "r": r,
        "s": s,
        "y": y,

        "t": t,
        "u": u,
        "v": v,

        "w": w
    }

    logger.info(f"Compatibility Matrix values: {compatibility_matrix_value}")

    output_serializer = MatrixCompability2OutputSerializer(data=compatibility_matrix_value)
    if not output_serializer.is_valid():
        logger.error(f"Validation errors: {output_serializer.errors}")
        return Response(output_serializer.errors, status=400)
    
    input_data = normalize_input_data(serializer.validated_data)

    if request.user.is_authenticated and hasattr(request.user, 'profile'):
        already_exists = UserCalculationHistory.objects.filter(
            profile=request.user.profile,
            input_data=input_data,
            category="compatibility"
        ).exists()
    
        if not already_exists:
            UserCalculationHistory.objects.create(
                profile=request.user.profile,
                input_data=input_data,
                result_data=compatibility_matrix_value,
                category="compatibility"
            )
    
    # Если пользователь авторизован, сохраняем в профиль
    # if request.user.is_authenticated and hasattr(request.user, 'profile'):
    #     UserCalculationHistory.objects.create(
    #         profile=request.user.profile,
    #         input_data=request.data,
    #         result_data=compatibility_matrix_value,
    #         category="compatibility" 
    #     )

    return Response(compatibility_matrix_value)

        

