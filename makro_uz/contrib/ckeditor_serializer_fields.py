from django.conf import settings
from rest_framework import serializers

SEARCH_PATTERN = 'href=\\"' + settings.MEDIA_URL + settings.CKEDITOR_UPLOAD_PATH
REPLACE_WITH = ('href=\\"{domain}' + settings.MEDIA_URL + settings.CKEDITOR_UPLOAD_PATH).format(
    domain=settings.SITE_DOMAIN)


class FixAbsolutePathSerializer(serializers.Field):

    def to_representation(self, value):
        text = value.replace(SEARCH_PATTERN, REPLACE_WITH)
        return text
