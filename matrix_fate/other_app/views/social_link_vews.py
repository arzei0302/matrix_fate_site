from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import AllowAny
from drf_spectacular.utils import extend_schema, OpenApiParameter
from other_app.serializers.social_link_serilizer import SocialLinksSerializer
from ..models import SocialLinks


@extend_schema(
    tags=["SocialLink"],
    summary="Получить ссылку на соц. сеть по id",
    description="Возвращает одну ссылку по id.",
    responses={200: SocialLinksSerializer},
)
class SocialLinkDetailView(RetrieveAPIView):
    queryset = SocialLinks.objects.all()
    serializer_class = SocialLinksSerializer
    permission_classes = [AllowAny]
