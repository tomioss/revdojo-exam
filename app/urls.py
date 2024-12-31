from rest_framework.routers import DefaultRouter

from app.views import StatisticsApiView, VehicleApiView, VehicleDetailsApiView


app_name = "app"

router = DefaultRouter()
router.register("vehicle", VehicleApiView, basename="vehicle")
router.register("statistics", StatisticsApiView, basename="statistics")
router.register("vehicle_details", VehicleDetailsApiView, basename="vehicle-details")

urlpatterns = router.urls

