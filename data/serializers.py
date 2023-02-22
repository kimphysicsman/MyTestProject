from rest_framework import serializers

from data.models import Data as DataModel


class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataModel
        fields = "__all__"