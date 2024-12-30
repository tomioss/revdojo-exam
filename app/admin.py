from django.contrib import admin

from app.models import Vehicle, Statistics


class VehicleAdmin(admin.ModelAdmin):
    model = Vehicle
    list_display = (
        "id",
        "vin",
        "stock_number",
        "start_date",
        "end_date",
        "status",
        "vehicle_type",
        "description",
        "price",
        "photos_count",
        "created_at",
        "updated_at",
    )


class StatisticsAdmin(admin.ModelAdmin):
    model = Statistics
    list_display = (
        "id",
        "source",
        "vdp_count",
        "srp_count",
        "vin",
        "created_at",
        "updated_at",
    )


admin.site.register(Vehicle, VehicleAdmin)
admin.site.register(Statistics, StatisticsAdmin)

