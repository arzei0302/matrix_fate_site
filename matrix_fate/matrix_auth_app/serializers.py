from rest_framework import serializers
from django.contrib.auth import get_user_model
from drf_spectacular.utils import extend_schema_field

from .models import EmailVerificationCode, UserCalculationHistory


User = get_user_model()


class EmailSerializer(serializers.Serializer):
    email = serializers.EmailField()
    def validate_email(self, value):
        """
        Проверяет, существует ли пользователь с таким email.
        Если нет, создает нового.
        """
        user, created = User.objects.get_or_create(email=value)
        return value


class VerifyCodeSerializer(serializers.Serializer):
    email = serializers.EmailField()
    code = serializers.CharField(max_length=6)

    def validate(self, data):
        """
        Проверяет, что код существует в базе данных.
        """
        email = data.get("email")
        code = data.get("code")

        try:
            user = User.objects.get(email=email)
            verification_entry = EmailVerificationCode.objects.filter(user=user, code=code).last()

            if not verification_entry:
                raise serializers.ValidationError("Неверный код.")

        except User.DoesNotExist:
            raise serializers.ValidationError("Пользователь не найден.")

        return data
    
    
class ProtectedSerializer(serializers.Serializer):
    message = serializers.CharField()


class LogoutSerializer(serializers.Serializer):
    refresh_token = serializers.CharField()

    def validate_refresh_token(self, value):
        if not value:
            raise serializers.ValidationError("Refresh токен обязателен.")
        return value

    
# class CalculationHistorySerializer(serializers.ModelSerializer):
#     profile = serializers.SerializerMethodField()
#     category = serializers.CharField(source='get_category_display')

#     class Meta:
#         model = UserCalculationHistory
#         fields = ['id', 'profile', 'input_data', 'result_data', 'category', 'created_at']

#     def get_profile(self, obj):
#         if obj.profile:
#             return {
#                 "id": obj.profile.id,
#                 "access_level": obj.profile.access_level,
#                 "email": obj.profile.user.email,
#             }
#         return None

class CalculationHistorySerializer(serializers.ModelSerializer):
    profile = serializers.SerializerMethodField()
    category = serializers.CharField(source='get_category_display')

    class Meta:
        model = UserCalculationHistory
        fields = ['id', 'profile', 'input_data', 'result_data', 'category', 'created_at']

    @extend_schema_field({
        'type': 'object',
        'properties': {
            'id': {'type': 'integer'},
            'access_level': {'type': 'string'},
            'email': {'type': 'string', 'format': 'email'},
        },
        'nullable': True
    })
    def get_profile(self, obj):
        if obj.profile:
            return {
                "id": obj.profile.id,
                "access_level": obj.profile.access_level,
                "email": obj.profile.user.email,
            }
        return None




