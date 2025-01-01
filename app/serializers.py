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


class SourceStatisticsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Statistics
        fields = ("source",)


class VehicleDetailsSerializer(serializers.ModelSerializer):
    total_vdp_count = serializers.IntegerField()
    total_srp_count = serializers.IntegerField()
    source = SourceStatisticsSerializer(source="statistics_set", many=True)

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
            "total_vdp_count",
            "total_srp_count",
            "source",
        )

