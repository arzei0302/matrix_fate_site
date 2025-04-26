


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import NotFound
from drf_spectacular.utils import extend_schema

from ..models import MessageSupport, PrivacyPolicy, PublicOfferAgreement
from matrix_fate.other_app.serializers.footer_serializers import MessageSupportSerializer, PrivacyPolicySerializer, PublicOfferAgreementSerializer



@extend_schema(
    tags=['Footer'],
    responses={200: MessageSupportSerializer}
)
class MessageSupportDetailView(APIView):
    """Получить сообщение в поддержку по ID"""
    
    serializer_class = MessageSupportSerializer
    
    def get(self, request, pk, *args, **kwargs):
        try:
            message = MessageSupport.objects.get(pk=pk)
        except MessageSupport.DoesNotExist:
            raise NotFound("Сообщение в поддержку не найдено")
        
        serializer = self.serializer_class(message)
        return Response(serializer.data, status=status.HTTP_200_OK)

@extend_schema(
    tags=['Footer'],
    responses={200: PrivacyPolicySerializer}
)
class PrivacyPolicyDetailView(APIView):
    """Получить политику конфиденциальности по ID"""
    
    serializer_class = PrivacyPolicySerializer
    
    def get(self, request, pk, *args, **kwargs):
        try:
            policy = PrivacyPolicy.objects.get(pk=pk)
        except PrivacyPolicy.DoesNotExist:
            raise NotFound("Политика конфиденциальности не найдена")
        
        serializer = self.serializer_class(policy)
        return Response(serializer.data, status=status.HTTP_200_OK)

@extend_schema(
    tags=['Footer'],
    responses={200: PublicOfferAgreementSerializer}
)
class PublicOfferAgreementDetailView(APIView):
    """Получить договор публичной оферты по ID"""
    
    serializer_class = PublicOfferAgreementSerializer
    
    def get(self, request, pk, *args, **kwargs):
        try:
            agreement = PublicOfferAgreement.objects.get(pk=pk)
        except PublicOfferAgreement.DoesNotExist:
            raise NotFound("Договор публичной оферты не найден")
        
        serializer = self.serializer_class(agreement)
        return Response(serializer.data, status=status.HTTP_200_OK)
