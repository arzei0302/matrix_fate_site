# matrix_fate/common/mixins.py
from rest_framework.response import Response
from rest_framework.status import HTTP_403_FORBIDDEN
from matrix_fate.common.permissions import is_active_paid_user


class PaidCategoryAccessMixin:
    """
    Проверяет, имеет ли пользователь доступ к платной категории.
    Если категория is_paid=True, а пользователь не подписан — вернёт Response 403.
    """

    def check_category_access(self, request, category):
        if category.is_paid and not is_active_paid_user(request.user):
            return Response(
                {
                    "category": {
                        "id": category.id,
                        "title": category.title,
                        "is_paid": category.is_paid,
                    }
                },
                status=HTTP_403_FORBIDDEN,
            )
        return None  # доступ разрешён
    


class PaidProgramAccessMixin:
    """
    Проверяет, имеет ли пользователь доступ к платной программе.
    Если программа is_paid=True, а пользователь не подписан — возвращает 403.
    """

    def check_program_access(self, request, program):
        if program.is_paid and not is_active_paid_user(request.user):
            return Response(
                {
                    "program": {
                        "id": program.id,
                        "title": getattr(program, "title", ""),
                        "is_paid": program.is_paid,
                    }
                },
                status=HTTP_403_FORBIDDEN,
            )
        return None

