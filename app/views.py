from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import mixins, viewsets
from rest_framework.permissions import IsAuthenticated

from app.filters import VehicleFilter 
from app.models import Vehicle
from app.serializers import VehicleSerializer


class VehicleApiView(mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Vehicle.objects.all().order_by("id")
    serializer_class = VehicleSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = VehicleFilter

