import logging
from django.core.mail import send_mail
from django.utils.timezone import now, timedelta
from django.utils import timezone
from django.contrib.auth import get_user_model
from drf_spectacular.utils import extend_schema
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenRefreshView

# from matrix_fate.config import settings
from matrix_fate.config import settings

from .models import EmailVerificationCode, UserCalculationHistory
from .serializers import (
    CalculationHistorySerializer, EmailSerializer, LogoutSerializer, 
    ProtectedSerializer, UserSubscriptionInfoResponseSerializer, VerifyCodeSerializer
    )
from .models import ACCESS_LEVEL_CHOICES, ACCESS_EXPIRATION_DAYS
# from matrix_auth_app.email_utils import send_email_brevo

User = get_user_model()
logger = logging.getLogger(__name__)

CODE_EXPIRATION_TIME = 5  # Время жизни кода (в минутах)


class SendCodeView(APIView):
    """Отправка кода на почту"""

    serializer_class = EmailSerializer
    @extend_schema(
            tags=['Auth'],
            description="Отправка кода на почту",
            )
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            
            user, created = User.objects.get_or_create(email=email)

            if created:
                logger.info(f'Создан новый пользователь: {user.email}')
            
            EmailVerificationCode.objects.filter(user=user).delete()

            code_entry = EmailVerificationCode.objects.create(user=user)

            logger.info(f'Попытка отправки письма на {email} с кодом {code_entry.code}')

            send_mail(
                'Confirmation code to log in to numerology-calculator.fi',
                f'Access code: {code_entry.code}',
                'fnumerology@gmail.com',
                [email],
                fail_silently=False,
)

            # send_mail(
            #     'Ваш код для входа',
            #     f'Ваш код: {code_entry.code}',
            #     settings.DEFAULT_FROM_EMAIL,
            #     [email],
            #     fail_silently=False,
            # )
            
            return Response({'detail': 'Код отправлен'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VerifyCodeView(APIView):
    """Проверка кода"""

    serializer_class = VerifyCodeSerializer

    @extend_schema(
            tags=['Auth'],
            description="Проверка кода",
            )
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            code = serializer.validated_data['code']

            try:
                user = User.objects.get(email=email)
                verification_entry = EmailVerificationCode.objects.filter(user=user, code=code).last()

                if not verification_entry:
                    return Response({'detail': 'Неверный код'}, status=status.HTTP_400_BAD_REQUEST)

                if now() - verification_entry.created_at > timedelta(minutes=CODE_EXPIRATION_TIME):
                    verification_entry.delete()
                    return Response({'detail': 'Код истек, запросите новый'}, status=status.HTTP_400_BAD_REQUEST)

                refresh = RefreshToken.for_user(user)

                verification_entry.delete()

                return Response({
                    'refresh': str(refresh),
                    'access': str(refresh.access_token)
                }, status=status.HTTP_200_OK)
            except User.DoesNotExist:
                return Response({'detail': 'Пользователь не найден'}, status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProtectedView(APIView):
    """Проверка JWT токена"""

    permission_classes = [IsAuthenticated]
    serializer_class = ProtectedSerializer 

    @extend_schema(
            tags=['Auth'],
            description="Проверка JWT токена",
            )
    def get(self, request):
        data = {"message": f"Привет, {request.user.email}! Вы успешно аутентифицированы."}
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@extend_schema(tags=['Auth'], description="Обновление JWT токена")
class CustomTokenRefreshView(TokenRefreshView):
    """Обновление JWT токена"""
    pass


class LogoutView(APIView):
    """Выход из аккаунта"""

    permission_classes = [IsAuthenticated]
    serializer_class = LogoutSerializer

    @extend_schema(
            tags=['Auth'],
            description="Выход из аккаунта",
            )
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            refresh_token = serializer.validated_data["refresh_token"]
            try:
                token = RefreshToken(refresh_token)
                token.blacklist()
                return Response(status=status.HTTP_205_RESET_CONTENT)
            except Exception as e:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class UserCalculationHistoryView(APIView):
    """Получение истории расчетов авторизованного пользователя"""
    permission_classes = [IsAuthenticated]

    @extend_schema(
        tags=['AuthProfile'],
        description="Получение истории расчетов авторизованного пользователя",
        responses={200: CalculationHistorySerializer(many=True)}
    )
    def get(self, request):
        calculations = UserCalculationHistory.objects.filter(profile=request.user.profile).order_by('-created_at')
        serializer = CalculationHistorySerializer(calculations, many=True)
        return Response(serializer.data, status=200)


class UserSubscriptionInfoView(APIView):
    """Получение информации о текущей подписке авторизованного пользователя"""
    permission_classes = [IsAuthenticated]

    @extend_schema(
        tags=['AuthProfile'],
        description="Получение информации о действующем абонементе авторизованного пользователя",
        # responses={200: 'application/json'},
        responses={200: UserSubscriptionInfoResponseSerializer},

        
    )
    def get(self, request):
        profile = request.user.profile

        now = timezone.now()
        is_active = (
            profile.access_expiration is None or
            profile.access_expiration > now
        )

        current_subscription = {
            'level': profile.access_level,
            'name': profile.get_access_level_display(),
            'expires_at': profile.access_expiration,
            'is_active': is_active
        }

        return Response({
            'current_subscription': current_subscription
        }, status=200)