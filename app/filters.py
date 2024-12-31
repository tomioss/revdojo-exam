from django_filters import rest_framework as filters

from app.models import Vehicle


class VehicleDetailsFilter(filters.FilterSet):
    date_range_gte = filters.DateTimeFilter(field_name="start_date", lookup_expr="gte")
    date_range_lte = filters.DateTimeFilter(field_name="start_date", lookup_expr="lte")

    class Meta:
        model = Vehicle
        fields = (
            "vin",
            "stock_number",
            "status",
            "vehicle_type",
        )

