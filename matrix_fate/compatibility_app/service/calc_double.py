from rest_framework import serializers
from drf_spectacular.utils import extend_schema
from rest_framework.decorators import api_view
from rest_framework.response import Response
import logging
from matrix_fate.compatibility_app.serializers.matrix_compatibility_program_serializers import MatrixCompatibilityProgramSerializer
from matrix_fate.compatibility_app.service.calc_double2 import calculate_compatibility, calculate_matrix
from matrix_fate.compatibility_app.service.calculator_matrix_compatibility_serializer import MatrixCompatibilityOutputSerializer
from matrix_fate.compatibility_app.service.service import get_matching_programs
from matrix_fate.matrix_auth_app.models import UserCalculationHistory
from matrix_fate.common.input_data import normalize_input_data

logger = logging.getLogger(__name__)


class CompatibilityMatrixAccessHandler:
    def filter_accessible_programs(self, request, programs):
        return programs  # не отрезаем платные — пусть отображаются


class MatrixDoubleInputSerializer(serializers.Serializer):
    day1 = serializers.IntegerField(min_value=1, max_value=31)
    month1 = serializers.IntegerField(min_value=1, max_value=12)
    year1 = serializers.IntegerField(min_value=1000, max_value=9999)
    day2 = serializers.IntegerField(min_value=1, max_value=31)
    month2 = serializers.IntegerField(min_value=1, max_value=12)
    year2 = serializers.IntegerField(min_value=1000, max_value=9999)

@extend_schema(
    tags=['Compatibility Matrix'],
    request=MatrixDoubleInputSerializer,
    responses={200: MatrixCompatibilityOutputSerializer},
)
@api_view(["POST"])
def calculate_full_compatibility_view(request):
    serializer = MatrixDoubleInputSerializer(data=request.data)
    if not serializer.is_valid():
        return Response(serializer.errors, status=400)

    day1 = serializer.validated_data["day1"]
    month1 = serializer.validated_data["month1"]
    year1 = serializer.validated_data["year1"]

    day2 = serializer.validated_data["day2"]
    month2 = serializer.validated_data["month2"]
    year2 = serializer.validated_data["year2"]

    matrix1 = calculate_matrix(day1, month1, year1)
    matrix2 = calculate_matrix(day2, month2, year2)
    compatibility_matrix = calculate_compatibility(matrix1, matrix2)

    matrix_values = {
        "category": "compatibility",
        "matrix1": matrix1,
        "matrix2": matrix2,
        "compatibility_matrix": compatibility_matrix
    }

    logger.info(f"Compatibility matrix values: {matrix_values}")

    flat_matrix = {"category": "compatibility", **compatibility_matrix}

    output_serializer = MatrixCompatibilityOutputSerializer(data=flat_matrix)
    if not output_serializer.is_valid():
        logger.error(f"Validation errors: {output_serializer.errors}")
        return Response(output_serializer.errors, status=400)

    input_data = normalize_input_data(serializer.validated_data)

    matched_programs = get_matching_programs(matrix_values)
    matched_programs = CompatibilityMatrixAccessHandler().filter_accessible_programs(
        request, matched_programs
    )

    serialized_programs = MatrixCompatibilityProgramSerializer(matched_programs, many=True,context={"request": request}).data
    matrix_values["matched_programs"] = serialized_programs

    if request.user.is_authenticated and hasattr(request.user, 'profile'):
        UserCalculationHistory.objects.update_or_create(
            profile=request.user.profile,
            input_data=input_data,
            category="compatibility",
            defaults={'result_data': matrix_values}
        )

    return Response({"matrix": matrix_values})

