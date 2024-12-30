from rest_framework.routers import DefaultRouter

from app.views import StatisticsApiView, VehicleApiView


app_name = "app"

router = DefaultRouter()
router.register("vehicle", VehicleApiView, basename="vehicle")
router.register("statistics", StatisticsApiView, basename="statistics")

urlpatterns = router.urls

