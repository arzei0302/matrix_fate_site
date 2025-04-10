from rest_framework.decorators import api_view
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema, OpenApiResponse
import logging
#
from common.input_data import normalize_input_data
from matrix_auth_app.models import UserCalculationHistory
from matrix_fate_app.serializers.matrix_fate_program_serializers import (
    MatrixFateInputSerializer, MatrixFateOutputSerializer, MatrixFateProgramSerializer)
from matrix_fate_app.service.service import get_matching_programs


logger = logging.getLogger(__name__)


def reduce_to_22(number: int) -> int:
    """Суммирует цифры числа, если оно больше 22."""
    while number > 22:
        number = sum(int(digit) for digit in str(number))
    return number


@extend_schema(
    tags=['Matrix_Fate'],
    request=MatrixFateInputSerializer,
    responses={
        200: MatrixFateOutputSerializer,
        400: OpenApiResponse(
            response={"error": "Invalid input data"},
            description="Invalid input data"
        )
    }
)


@api_view(["POST"])
def calculate_matrix_view(request):
    """Категории: ('matrix_fate', 'finance', 'compatibility', 'child')"""
    serializer = MatrixFateInputSerializer(data=request.data)
    if not serializer.is_valid():
        return Response(serializer.errors, status=400)
    
    birth_day = serializer.validated_data["day"]
    birth_month = serializer.validated_data["month"]
    birth_year = serializer.validated_data["year"]
    category = serializer.validated_data["category"]


    if not (1 <= birth_month <= 12):
        return Response({"error": "Месяц должен быть в диапазоне 1-12"}, status=400)
    
    if category not in ["matrix_fate", "finance", "compatibility", "child"]:
        return Response({"error": "Некорректная категория"}, status=400)
    
    # Логика матрицы судьбы
    a = reduce_to_22(birth_day)
    b = birth_month
    c = reduce_to_22(birth_year)
    d = reduce_to_22(a + b + c)
    e = reduce_to_22(a + b + c + d)
    f = reduce_to_22(a + b)
    g = reduce_to_22(b + c)
    h = reduce_to_22(c + d)
    i = reduce_to_22(d + a)
    e2 = reduce_to_22(f + g + h + i)
    e1 = reduce_to_22(e + e2)
    a2 = reduce_to_22(a + e)
    a1 = reduce_to_22(a + a2)
    n = reduce_to_22(a2 + e)
    b2 = reduce_to_22(b + e)
    b1 = reduce_to_22(b + b2)
    m = reduce_to_22(b2 + e)
    c2 = reduce_to_22(c + e)
    c1 = reduce_to_22(c + c2)
    d2 = reduce_to_22(d + e)
    d1 = reduce_to_22(d + d2)
    f2 = reduce_to_22(f + e)
    f1 = reduce_to_22(f + f2)
    g2 = reduce_to_22(g + e)
    g1 = reduce_to_22(g + g2)
    h2 = reduce_to_22(h + e)
    h1 = reduce_to_22(h + h2)
    i2 = reduce_to_22(i + e)
    i1 = reduce_to_22(i + i2)
    j = reduce_to_22(d2 + c2)
    k = reduce_to_22(d2 + j)
    l = reduce_to_22(c2 + j)
    # Личная и социальная матрица
    r = reduce_to_22(b + d)
    s = reduce_to_22(a + c)
    y = reduce_to_22(r + s)
    t = reduce_to_22(f + h)
    u = reduce_to_22(g + i)
    v = reduce_to_22(t + u)
    w = reduce_to_22(y + v)
    x = reduce_to_22(w + v)
    #карта здоровья:
    #физика/земная линия
    o7 = reduce_to_22(a)
    o6 = reduce_to_22(a1)
    o5 = reduce_to_22(a2)
    o4 = reduce_to_22(n)
    o3 = reduce_to_22(e)
    o2 = reduce_to_22(c2)
    o1 = reduce_to_22(c)
    o = reduce_to_22(a + a1 + a2 + n + e + c2 + c)
    #энергия/небесная линия
    p7 = reduce_to_22(b)
    p6 = reduce_to_22(b1)
    p5 = reduce_to_22(b2)
    p4 = reduce_to_22(m)
    p3 = reduce_to_22(e)
    p2 = reduce_to_22(d2)
    p1 = reduce_to_22(d)
    p = reduce_to_22(b + b1 + b2 + m + e + d2 + d)
    #эмоции/сумма неба и земли
    q7 = reduce_to_22(a + b)
    q6 = reduce_to_22(a1 + b1)
    q5 = reduce_to_22(a2 + b2)
    q4 = reduce_to_22(n + m)
    q3 = reduce_to_22(e + e)
    q2 = reduce_to_22(c2 + d2)
    q1 = reduce_to_22(c + d)
    q = reduce_to_22(q7 + q6 + q5 + q4 + q3 + q2 + q1)
    # Года
    # a
    a5    = reduce_to_22(a + f)
    a2_3  = reduce_to_22(a + a5)
    a3_4  = reduce_to_22(a2_3 + a5)
    a1_2  = reduce_to_22(a + a2_3)
    a7_8  = reduce_to_22(f + a5)
    a8_9  = reduce_to_22(a7_8 + f)
    a6_7  = reduce_to_22(a5 + a7_8)
    # f
    f15    = reduce_to_22(f + b)
    f12_13 = reduce_to_22(f + f15)
    f13_14 = reduce_to_22(f12_13 + f15)
    f11_12 = reduce_to_22(f + f12_13)
    f17_18 = reduce_to_22(b + f15)
    f18_19 = reduce_to_22(b + f17_18)
    f16_17 = reduce_to_22(f15 + f17_18)
    # b
    b25    = reduce_to_22(b + g)
    b22_23 = reduce_to_22(b + b25)
    b23_24 = reduce_to_22(b22_23 + b25)
    b21_22 = reduce_to_22(b + b22_23)
    b27_28 = reduce_to_22(g + b25)
    b28_29 = reduce_to_22(g + b27_28)
    b26_27 = reduce_to_22(b25 + b27_28)
    # g
    g35    = reduce_to_22(g + c)
    g32_33 = reduce_to_22(g + g35)
    g33_34 = reduce_to_22(g32_33 + g35)
    g31_32 = reduce_to_22(g + g32_33)
    g37_38 = reduce_to_22(c + g35)
    g38_39 = reduce_to_22(c + g37_38)
    g36_37 = reduce_to_22(g35 + g37_38)
    # c
    c45    = reduce_to_22(c + h)
    c42_43 = reduce_to_22(c + c45)
    c43_44 = reduce_to_22(c42_43 + c45)
    c41_42 = reduce_to_22(c + c42_43)
    c47_48 = reduce_to_22(h + c45)
    c48_49 = reduce_to_22(h + c47_48)
    c46_47 = reduce_to_22(c45 + c47_48)
    # h
    h55    = reduce_to_22(h + d)
    h52_53 = reduce_to_22(h + h55)
    h53_54 = reduce_to_22(h52_53 + h55)
    h51_52 = reduce_to_22(h + h52_53)
    h57_58 = reduce_to_22(d + h55)
    h58_59 = reduce_to_22(d + h57_58)
    h56_57 = reduce_to_22(h55 + h57_58)
    # d
    d65    = reduce_to_22(d + i)
    d62_63 = reduce_to_22(d + d65)
    d63_64 = reduce_to_22(d62_63 + d65)
    d61_62 = reduce_to_22(d + d62_63)
    d67_68 = reduce_to_22(i + d65)
    d68_69 = reduce_to_22(i + d67_68)
    d66_67 = reduce_to_22(d65 + d67_68)
    # i
    i75    = reduce_to_22(i + a)
    i72_73 = reduce_to_22(i + i75)
    i73_74 = reduce_to_22(i72_73 + i75)
    i71_72 = reduce_to_22(i + i72_73)
    i77_78 = reduce_to_22(a + i75)
    i78_79 = reduce_to_22(a + i77_78)
    i76_77 = reduce_to_22(i75 + i77_78)

    
    matrix_values = {
        "category": category,  
        "a": a, "b": b, "c": c, "d": d, "e": e, "e1": e1, "e2": e2,
        "f": f, "g": g, "h": h, "i": i,
        "a1": a1, "a2": a2, "n": n,
        "b1": b1, "b2": b2, "m": m,
        "c1": c1, "c2": c2,
        "d1": d1, "d2": d2,
        "f1": f1, "f2": f2,
        "g1": g1, "g2": g2,
        "h1": h1, "h2": h2,
        "i1": i1, "i2": i2,
        "j": j, "k": k, "l": l,
        "r": r, "s": s, "y": y, "t": t, "u": u, "v": v, "w": w, "x": x,
        "o": o, "o1": o1, "o2": o2, "o3": o3, "o4": o4, "o5": o5, "o6": o6, "o7": o7,
        "p": p, "p1": p1, "p2": p2, "p3": p3, "p4": p4, "p5": p5, "p6": p6, "p7": p7,
        "q": q, "q1": q1, "q2": q2, "q3": q3, "q4": q4, "q5": q5, "q6": q6, "q7": q7,
        "a1_2": a1_2, "a2_3": a2_3, "a3_4": a3_4, "a5": a5, "a6_7": a6_7, "a7_8": a7_8, "a8_9": a8_9,
        "f11_12": f11_12, "f12_13": f12_13, "f13_14": f13_14, "f15": f15, "f16_17": f16_17, "f17_18": f17_18, "f18_19": f18_19,
        "b21_22": b21_22, "b22_23": b22_23, "b23_24": b23_24, "b25": b25, "b26_27": b26_27, "b27_28": b27_28, "b28_29": b28_29,
        "g31_32": g31_32, "g32_33": g32_33, "g33_34": g33_34, "g35": g35, "g36_37": g36_37, "g37_38": g37_38, "g38_39": g38_39,
        "c41_42": c41_42, "c42_43": c42_43, "c43_44": c43_44, "c45": c45, "c46_47": c46_47, "c47_48": c47_48, "c48_49": c48_49,
        "h51_52": h51_52, "h52_53": h52_53, "h53_54": h53_54, "h55": h55, "h56_57": h56_57, "h57_58": h57_58, "h58_59": h58_59,
        "d61_62": d61_62, "d62_63": d62_63, "d63_64": d63_64, "d65": d65, "d66_67": d66_67, "d67_68": d67_68, "d68_69": d68_69,
        "i71_72": i71_72, "i72_73": i72_73, "i73_74": i73_74, "i75": i75, "i76_77": i76_77, "i77_78": i77_78, "i78_79": i78_79
    }

    logger.info(f"Matrix values: {matrix_values}")

    output_serializer = MatrixFateOutputSerializer(data=matrix_values)
    if not output_serializer.is_valid():
        logger.error(f"Validation errors: {output_serializer.errors}")
        return Response(output_serializer.errors, status=400)

    input_data = normalize_input_data(serializer.validated_data)

    if request.user.is_authenticated and hasattr(request.user, 'profile'):
        already_exists = UserCalculationHistory.objects.filter(
            profile=request.user.profile,
            input_data=input_data,
            category=category
        ).exists()
    
        if not already_exists:
            UserCalculationHistory.objects.create(
                profile=request.user.profile,
                input_data=input_data,
                result_data=matrix_values,
                category=category
            )

    matched_programs = get_matching_programs(matrix_values)
    serialized_programs = MatrixFateProgramSerializer(matched_programs, many=True).data

    return Response({
        "matrix": matrix_values,
        "matched_programs": serialized_programs
    })

