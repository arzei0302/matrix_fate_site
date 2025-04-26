from rest_framework import serializers

from matrix_fate.other_app.models import MessageSupport, PrivacyPolicy, PublicOfferAgreement



class MessageSupportSerializer(serializers.ModelSerializer):
    class Meta:
        model = MessageSupport
        fields = ['title', 'description', 'reference']

class PrivacyPolicySerializer(serializers.ModelSerializer):
    class Meta:
        model = PrivacyPolicy
        fields = ['title', 'description']

class PublicOfferAgreementSerializer(serializers.ModelSerializer):
    class Meta:
        model = PublicOfferAgreement
        fields = ['title', 'description']
