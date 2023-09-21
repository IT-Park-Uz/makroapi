from rest_framework import serializers

from common.news.models import Location, Region


class RegionCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ['id', 'title']


class LocationCreateSerializer(serializers.ModelSerializer):
    region = RegionCreateSerializer()

    class Meta:
        model = Location
        fields = ['id', 'region', 'address', 'longitude', 'latitude', 'startDate', 'endDate']
