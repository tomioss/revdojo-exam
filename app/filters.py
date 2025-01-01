from datetime import datetime

from django.db.models import Sum, Prefetch, OuterRef
from django.db.models.functions import Coalesce

from django_filters import rest_framework as filters

from app.models import Vehicle, Statistics


class VehicleDetailsFilter(filters.FilterSet):
    date_range = filters.CharFilter(method="filter_date_range")
    source = filters.CharFilter(method="filter_source")

    class Meta:
        model = Vehicle
        fields = (
            "vin",
            "stock_number",
            "status",
            "vehicle_type",
        )

    def _get_vehicle_queryset(self, queryset, stats_qs):
        total_stats_qs = stats_qs.filter(vin_id=OuterRef("pk")).values("vin_id").annotate(
            total_vdp_count=Sum("vdp_count"),
            total_srp_count=Sum("srp_count")
        )

        return queryset.prefetch_related(Prefetch("statistics_set", queryset=stats_qs)).annotate(
            total_vdp_count=Coalesce(total_stats_qs.values("total_vdp_count"), 0),
            total_srp_count=Coalesce(total_stats_qs.values("total_srp_count"), 0)
        ).exclude(statistics__isnull=True)

    def filter_date_range(self, queryset, name, value):
        if value:
            try:
                date_format = "%Y-%m-%d"
                start_date_str, end_date_str = value.split(",")

                start_date = datetime.strptime(start_date_str, date_format).date()
                end_date = datetime.strptime(end_date_str, date_format).date()

                stats_qs = Statistics.objects.filter(date__gte=start_date, date__lte=end_date)
                queryset = queryset.filter(statistics__date__gte=start_date, statistics__date__lte=end_date)
                return self._get_vehicle_queryset(queryset, stats_qs)
            except ValueError:
                return queryset.none()

        return queryset

    def filter_source(self, queryset, name, value):
        if value:
            try:
                stats_qs = Statistics.objects.filter(source=value)
                queryset = queryset.filter(statistics__source=value)
                return self._get_vehicle_queryset(queryset, stats_qs)
            except ValueError:
                return queryset.none()

        return queryset

