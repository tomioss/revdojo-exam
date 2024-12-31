from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import mixins, viewsets
from rest_framework.permissions import IsAuthenticated

from app.filters import VehicleDetailsFilter
from app.models import Vehicle, Statistics
from app.serializers import VehicleDetailsSerializer, VehicleSerializer, StatisticsSerializer


class VehicleApiView(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet
):
    permission_classes = (IsAuthenticated,)
    queryset = Vehicle.objects.all().order_by("id")
    serializer_class = VehicleSerializer


class StatisticsApiView(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet
):
    permission_classes = (IsAuthenticated,)
    queryset = Statistics.objects.all().order_by("id")
    serializer_class = StatisticsSerializer


class VehicleDetailsApiView(mixins.ListModelMixin, viewsets.GenericViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Vehicle.objects.filter(status=Vehicle.ON_SALE).order_by("id")
    serializer_class = VehicleDetailsSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = VehicleDetailsFilter

