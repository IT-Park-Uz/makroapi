from rest_framework import serializers

from common.news.models import News, NewsCatalog
from config.settings.base import env


class NewsCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ['id', 'title', 'description', 'photo']


class NewsListSerializer(serializers.ModelSerializer):
    photo_small = serializers.ImageField(read_only=True)
    photo_medium = serializers.SerializerMethodField()

    def get_photo_medium(self, news):
        if news.photo_medium and not "http" in news.photo_medium:
            return env('BASE_URL') + news.photo_medium.url
        return None

    class Meta:
        model = News
        fields = ['id', 'title', 'description', 'photo_small', 'photo_medium', 'created_at']


class NewsCatalogImagesSerializer(serializers.ModelSerializer):
    photo_uz = serializers.SerializerMethodField()
    photo_ru = serializers.SerializerMethodField()

    def get_photo_uz(self, news):
        if news.photo_uz and not "http" in news.photo_uz:
            return env('BASE_URL') + news.photo_uz.url
        return None

    def get_photo_ru(self, news):
        if news.photo_ru and not "http" in news.photo_ru:
            return env('BASE_URL') + news.photo_ru.url
        return None

    class Meta:
        model = NewsCatalog
        fields = ['id', 'photo_uz', 'photo_ru']


class NewsDetailSerializer(serializers.ModelSerializer):
    photo_medium = serializers.SerializerMethodField()
    newsCatalog = NewsCatalogImagesSerializer(many=True)

    def get_photo_medium(self, news):
        if news.photo_medium and not "http" in news.photo_medium:
            return env('BASE_URL') + news.photo_medium.url
        return None

    class Meta:
        model = News
        fields = ['id', 'title', 'description', 'photo_medium', 'newsCatalog', 'created_at']
