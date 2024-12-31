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


class VehicleDetailsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Vehicle
        fields = (
            "vin",
            "stock_number",
            "start_date",
            "vehicle_type",
            "description",
            "price",
            "photos_count",
        )

