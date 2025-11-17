from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from network.models import ContactsFactory, Network, ProductsFactory


class NetworkTestCase(APITestCase):
    def setUp(self):
        """Подготовка данных для тестов"""
        self.user = User.objects.create_user(
            username="test_name", password="test_password"
        )

        self.client.force_authenticate(user=self.user)

        self.contacts = ContactsFactory.objects.create(
            email_cont="test@mail.com",
            country_cont="test_country",
            city_cont="test_city",
            street_cont="test_street",
            number_phone_cont="test_phone",
        )

        self.products = ProductsFactory.objects.create(
            name_pr="test_name", models_pr="test_model", release_pr="1234-01-23"
        )

        self.network = Network.objects.create(
            name_fact="test",
            level=1,
            contacts_fact=self.contacts,
            time_create_fact="13:06:20",
        )
        self.new_data = {
            "id": 1,
            "level": 0,
            "name_fact": "ТМК",
            "debt_fact": "13.20",
            "time_create_fact": "13:06:20",
            "contacts_fact": 1,
            "products_fact": [1],
        }

    def test_network_create(self):
        """Тестирование создание новой сети"""
        response = self.client.post(
            reverse("network:network_create"), self.new_data, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_network_list(self):
        """Тестирование просмотра списка сетей"""
        response = self.client.get(reverse("network:network_list"), format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_network_detail(self):
        """Тестирование просмотра подробной информации об одной сети"""
        response = self.client.get(
            reverse("network:network_detail", kwargs={"pk": self.network.pk}),
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_network_update(self):
        """Тестирование редактирования сети"""
        self.new_data_2 = {
            "level": 2,
            "name_fact": "ТМК_2",
        }
        response = self.client.patch(
            reverse("network:network_update", kwargs={"pk": self.network.pk}),
            data=self.new_data_2,
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_network_delete(self):
        """Тестирование удаления сети"""
        response = self.client.delete(
            reverse("network:network_delete", kwargs={"pk": self.network.pk}),
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
