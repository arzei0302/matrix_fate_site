import logging
from celery import shared_task
from django.utils.timezone import localtime
from .models import Profile

logger = logging.getLogger(__name__)

@shared_task
def check_expired_profiles():
    now = localtime()
    logger.info(f"Проверка профилей на {now}")

    expired_profiles = Profile.objects.filter(
        access_expiration__isnull=False,
        access_expiration__lte=now,
        access_level__in=['level3', 'level4']
    )

    if not expired_profiles.exists():
        logger.info("Нет профилей для перевода на бесплатный уровень")
        return

    for profile in expired_profiles:
        logger.info(f"Перевожу профиль {profile.user.email} на бесплатный уровень")
        profile.access_level = 'level1'
        profile.access_expiration = None
        profile.save()
