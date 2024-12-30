from django.db import models


class Vehicle(models.Model):
    ON_SALE = "ONS"
    SOLD = "SLD"
    STATUS_CHOICES = {
        ON_SALE: "On Sale",
        SOLD: "Sold",
    }
    USED = "USED"
    NEW = "NEW"
    VEHICLE_TYPE_CHOICES = {
        USED: "Used",
        NEW: "New",
    }
    vin = models.CharField(max_length=17)
    stock_number = models.CharField(max_length=10)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    status = models.CharField(
        max_length=3,
        choices=STATUS_CHOICES,
    )
    vehicle_type = models.CharField(
        max_length=4,
        choices=VEHICLE_TYPE_CHOICES,
    )
    description = models.TextField()
    price = models.FloatField()
    photos_count = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Statistics(models.Model):
    source = models.CharField(max_length=255)
    vdp_count = models.IntegerField()
    srp_count = models.IntegerField()
    vin = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

