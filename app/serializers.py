from rest_framework import serializers

from app.models import Vehicle, Statistics


class VehicleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Vehicle
        fields = "__all__"


class StatisticsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Statistics
        fields = "__all__"

