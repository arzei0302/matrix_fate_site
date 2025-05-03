import logging
from matrix_fate.compatibility_app.models import MatrixCompatibilityProgram

print(f"LOGGER NAME: {__name__}")

logger = logging.getLogger(__name__)


def get_matching_programs(matrix_values):

    matched = []
    
    compatibility_matrix = matrix_values.get("compatibility_matrix", {})

    for program in MatrixCompatibilityProgram.objects.all():
        val1 = compatibility_matrix.get(program.marker_1_name)
        val2 = compatibility_matrix.get(program.marker_2_name)
        val3 = compatibility_matrix.get(program.marker_3_name)

        if (
            val1 == program.marker_1_value and
            val2 == program.marker_2_value and
            val3 == program.marker_3_value
        ):
            matched.append(program)

    return matched
