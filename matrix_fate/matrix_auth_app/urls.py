from django.urls import path

from .views import (
    CustomTokenRefreshView, LogoutView, ProtectedView, SendCodeView, 
    UserCalculationHistoryView, VerifyCodeView, UserSubscriptionInfoView
    )

urlpatterns = [
    path('send-code/', SendCodeView.as_view(), name='send-code'),
    path('verify-code/', VerifyCodeView.as_view(), name='verify-code'),
    path('token/refresh/', CustomTokenRefreshView.as_view(), name='token_refresh'),
    path('protected-endpoint/', ProtectedView.as_view(), name='protected-endpoint'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('history/', UserCalculationHistoryView.as_view(), name='calculation_history'),
    path('api/profile/subscription-info/', UserSubscriptionInfoView.as_view(), name='subscription-info'),
]


# from matrix_auth_app.models import Profile
# p = Profile.objects.get(user__email="kabulov.arz@gmail.com")
# print(p.access_level, p.access_expiration)

