from django.conf import settings
from rest_framework import serializers

SEARCH_PATTERN = settings.MEDIA_URL + settings.CKEDITOR_UPLOAD_PATH
REPLACE_WITH = settings.BASE_URL + settings.MEDIA_URL + settings.CKEDITOR_UPLOAD_PATH


class FixAbsolutePathSerializer(serializers.Field):

    def to_representation(self, value):
        text = value.replace(SEARCH_PATTERN, REPLACE_WITH)
        return text
