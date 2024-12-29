from django_filters import rest_framework as filters

from app.models import Vehicle


class VehicleFilter(filters.FilterSet):

    class Meta:
        model = Vehicle
        fields = (
            "vin",
            "stock_number",
            "vehicle_type",
        )

