# from rest_framework.permissions import BasePermission
# from django.utils import timezone


# class IsActivePaidUser(BasePermission):
#     """
#     Доступ разрешён только если:
#     - пользователь авторизован,
#     - access_level в ['level2', 'level3', 'level4'],
#     - access_expiration установлена и не истекла.
#     """

#     allowed_levels = ['level2', 'level3', 'level4']

#     def has_permission(self, request, view):
#         user = request.user
#         if not user.is_authenticated:
#             return False

#         profile = getattr(user, 'profile', None)
#         if not profile:
#             return False

#         if profile.access_level not in self.allowed_levels:
#             return False

#         if profile.access_expiration is None:
#             return False

#         if profile.access_expiration <= timezone.now():
#             return False

#         return True
    

from rest_framework.permissions import BasePermission
from django.utils import timezone


class IsActivePaidUser(BasePermission):
    """
    Доступ разрешён только если:
    - пользователь авторизован,
    - access_level в ['level2', 'level3', 'level4'],
    - access_expiration установлена и не истекла.
    """

    allowed_levels = ['level2', 'level3', 'level4']

    def has_permission(self, request, view):
        return is_active_paid_user(request.user)


def is_active_paid_user(user):
    """
    Проверка, что пользователь авторизован и имеет активную подписку.
    Синхронизировано с IsActivePaidUser.
    """
    if not user.is_authenticated:
        return False

    profile = getattr(user, 'profile', None)
    if not profile:
        return False

    if profile.access_level not in IsActivePaidUser.allowed_levels:
        return False

    if not profile.access_expiration or profile.access_expiration <= timezone.now():
        return False

    return True


