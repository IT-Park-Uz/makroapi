from rest_framework import serializers

from common.ferma.models import Toys


class ToysListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Toys
        fields = "__all__"
