from rest_framework import serializers

from common.news.models import News
from config.settings.base import env


class NewsCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ['id', 'title', 'description', 'photo']


class NewsListSerializer(serializers.ModelSerializer):
    photo_small = serializers.ImageField(read_only=True)

    class Meta:
        model = News
        fields = ['id', 'title', 'description', 'photo_small', 'created_at']


class NewsDetailSerializer(serializers.ModelSerializer):
    photo_medium = serializers.SerializerMethodField()

    def get_photo_medium(self, news):
        if news.photo_medium and not "http" in news.photo_medium:
            return env('BASE_URL') + news.photo_medium.url
        return None

    class Meta:
        model = News
        fields = ['id', 'title', 'description', 'photo_medium', 'created_at']
