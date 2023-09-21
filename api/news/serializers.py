from rest_framework import serializers

from common.news.models import News


class NewsCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ['id', 'title', 'description', 'videoURL', 'photo', 'status', 'startDate', 'endDate']


class NewsListSerializer(serializers.ModelSerializer):
    photo_small = serializers.ImageField(read_only=True)

    class Meta:
        model = News
        fields = ['id', 'title', 'videoURL', 'photo_small', 'status']


class NewsDetailSerializer(serializers.ModelSerializer):
    photo_medium = serializers.ImageField(read_only=True)

    class Meta:
        model = News
        fields = ['id', 'title', 'description', 'videoURL', 'photo_medium', 'status', 'startDate', 'endDate']
