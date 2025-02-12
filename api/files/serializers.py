from rest_framework import serializers

from common.files.models import Offerta


class OffertaListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Offerta
        fields = "__all__"
