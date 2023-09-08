from rest_framework import serializers

from common.news.models import Location


class LocationCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ['id', 'guid', 'longitude', 'latitude']
