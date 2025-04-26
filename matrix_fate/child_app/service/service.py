
from matrix_fate.child_app.models import MatrixChildProgram


def get_matching_programs(matrix_values):
    matched = []

    for program in MatrixChildProgram.objects.all():
        val1 = matrix_values.get(program.marker_1_name)
        val2 = matrix_values.get(program.marker_2_name)
        val3 = matrix_values.get(program.marker_3_name)

        if (
            val1 == program.marker_1_value and
            val2 == program.marker_2_value and
            val3 == program.marker_3_value
        ):
            matched.append(program)
    
    return matched
