from rest_framework import serializers
from other_app.models import SocialLinks


class SocialLinksSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialLinks
        fields = "__all__"