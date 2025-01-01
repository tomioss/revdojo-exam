from datetime import date

from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone

from rest_framework import status
from rest_framework.test import APITestCase

from app.models import Vehicle, Statistics


def create_user(username, password):
    user = User.objects.create_user(username)
    user.set_password(password)
    user.save()

def create_vehicle(vin, stock_number, start_date, end_date, status, vehicle_type):
    return Vehicle.objects.create(
        vin=vin,
        stock_number=stock_number,
        start_date=start_date,
        end_date=end_date,
        status=status,
        vehicle_type=vehicle_type,
        description="Description",
        price=100,
        photos_count=1,
    )

def create_statistics(date, source, vdp_count, srp_count, vin):
    return Statistics.objects.create(
        date=date,
        source=source,
        vdp_count=vdp_count,
        srp_count=srp_count,
        vin=vin,
    )


class VehicleApiViewTest(APITestCase):
    url = reverse("app:vehicle-list")

    def _login_user(self):
        username = "username"
        password = "password"
        create_user(username, password)
        self.assertTrue(self.client.login(username=username, password=password))

    def setUp(self):
        vehicle = create_vehicle("vin1", "stock1", timezone.now(), None, Vehicle.ON_SALE, Vehicle.NEW)
        self.detail_url = reverse("app:vehicle-detail", args=[vehicle.id])
        # create_vehicle("vin3", "stock2", timezone.now(), None, Vehicle.ON_SALE, Vehicle.USED)

        self._login_user()

    def test_list(self):
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = response.json()
        self.assertEqual(data["count"], 1)
        self.assertEqual(data["results"][0]["vin"], "vin1")

    def test_detail(self):
        response = self.client.get(self.detail_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = response.json()
        self.assertEqual(data["vin"], "vin1")

    def test_update_patch(self):
        data = {
            "vin": "vin1-1"
        }
        response = self.client.patch(self.detail_url, data=data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = response.json()
        self.assertEqual(data["vin"], "vin1-1")

    def test_delete(self):
        response = self.client.delete(self.detail_url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEquals(Vehicle.objects.all().count(), 0)


class StatisticsApiViewTest(APITestCase):
    url = reverse("app:statistics-list")

    def _login_user(self):
        username = "username"
        password = "password"
        create_user(username, password)
        self.assertTrue(self.client.login(username=username, password=password))

    def setUp(self):
        vehicle = create_vehicle("vin1", "stock1", timezone.now(), None, Vehicle.ON_SALE, Vehicle.NEW)
        statistics = create_statistics(timezone.now(), "src1", 1, 1, vehicle)
        self.detail_url = reverse("app:statistics-detail", args=[statistics.id])

        self._login_user()

    def test_list(self):
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = response.json()
        self.assertEqual(data["count"], 1)
        self.assertEqual(data["results"][0]["source"], "src1")

    def test_detail(self):
        response = self.client.get(self.detail_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = response.json()
        self.assertEqual(data["source"], "src1")

    def test_update_patch(self):
        data = {
            "source": "src1-1"
        }
        response = self.client.patch(self.detail_url, data=data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = response.json()
        self.assertEqual(data["source"], "src1-1")

    def test_delete(self):
        response = self.client.delete(self.detail_url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEquals(Statistics.objects.all().count(), 0)
