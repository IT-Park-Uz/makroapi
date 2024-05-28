from rest_framework import serializers

from common.news.models import Location, Region, District


class DistrictCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = District
        fields = ['id', 'title']


class RegionCreateSerializer(serializers.ModelSerializer):
    districts = serializers.SerializerMethodField()

    def get_districts(self, obj) -> DistrictCreateSerializer(many=True):
        return DistrictCreateSerializer(obj.districts, many=True).data

    class Meta:
        model = Region
        fields = ['id', 'title', 'districts']


class LocationCreateSerializer(serializers.ModelSerializer):
    district = DistrictCreateSerializer()

    class Meta:
        model = Location
        fields = ['id', 'district', 'title', 'address', 'longitude', 'latitude', 'open', 'close']
