from django.test import TestCase
from rest_framework.test import APIRequestFactory, APITestCase, APIClient
from rest_framework import status
from django.urls import reverse
import os
import json
import django

from main_store.views import BuketList, LikeList, like_create_view, bucket_create_view, ItemViewSet
from main_store.models import User, Items, Pictures, Buket

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "fetrisa_toy.settings")
django.setup()


class ItemViewSetTestCase(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = ItemViewSet.as_view({"get": "list", "post": "create"})
        self.user = User.objects.create_user(email="testuser@mail.ru", password="testpassword")
        self.url = reverse("items-list")
        self.client.force_authenticate(user=self.user)

    def test_list_items(self):
        request = self.factory.get(self.url)
        response = self.view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class AllItemViewSetTestCase(APITestCase):
    def setUp(self):
        self.item = Items.objects.create(
            name="test", number=18, size=10, price=500, description="test", category="test"
        )
        self.picture = Pictures.objects.create(item=self.item, picture="test.jpg")

    def test_retrieve_item_picture(self):
        url = reverse("item-detail", kwargs={"id": self.item.id})
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_nonexistent_item_picture(self):
        url = reverse("item-detail", kwargs={"id": 999})  # Несуществующий ID
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class RegistrationViewTestCase(APITestCase):
    def setUp(self):
        self.url = reverse("register")
        self.invalid_payload = {
            "email": "testuser",
            "password": "test123",
        }

    def test_registration_view_with_invalid_payload(self):
        response = self.client.post(self.url, data=self.invalid_payload)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class UserListTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(email="testuser@mail.ru", password="test")
        self.url = reverse("user_list")
        self.client.force_authenticate(user=self.user)

    def test_user_list_view(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)  # Проверяем код ответа
        self.assertEqual(len(response.data), 1)  # Проверяем количество пользователей в ответе
        self.assertEqual(response.data[0]["email"], self.user.email)  # Проверяем ожидаемые данные пользователя


class UserDetailViewTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(email="testuser@mail.ru", password="test")
        self.url = reverse("user-detail", kwargs={"pk": self.user.pk})
        self.client.force_authenticate(user=self.user)

    def test_user_detail_view(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)  # Проверяем код ответа
        self.assertEqual(response.data["email"], self.user.email)  # Проверяем ожидаемые данные пользователя


class BucketCreateViewTestCase(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.user = User.objects.create(email="testuser@mail.ru", password="test")
        self.item = Items.objects.create(
            name="test", number=18, size=10, price=500, description="test", category="test"
        )

    def test_like_create_view(self):
        request_data = {"user": str(self.user.id), "item": str(self.item.id)}
        request = self.factory.post("http://127.0.0.1:8000/bucket/create/", data=request_data, format="json")
        response = bucket_create_view(request)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, {"success": True})


class LikeCreateViewTestCase(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.user = User.objects.create(email="testuser@mail.ru", password="test")
        self.item = Items.objects.create(
            name="test", number=18, size=10, price=500, description="test", category="test"
        )

    def test_like_create_view(self):
        request_data = {"user": str(self.user.id), "item": str(self.item.id)}
        request = self.factory.post("http://127.0.0.1:8000/like/create/", data=request_data, format="json")
        response = like_create_view(request)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, {"success": True})


class BuketListViewTestCase(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()

    def test_buket_list_view(self):
        url = reverse("buket-user-list", kwargs={"user_id": 1})
        request = self.factory.get(url)
        response = BuketList.as_view()(request, user_id=1)

        self.assertEqual(response.status_code, status.HTTP_200_OK)


class LikeListViewTestCase(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()

    def test_like_list_view(self):
        url = reverse("like-user-list", kwargs={"user_id": 1})
        request = self.factory.get(url)
        response = LikeList.as_view()(request, user_id=1)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
