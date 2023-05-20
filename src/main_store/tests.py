from django.test import TestCase
from rest_framework.test import APIClient, APIRequestFactory
from rest_framework import status
from django.urls import reverse
from rest_framework.test import APITestCase
import os
import django

from main_store.views import BuketList, LikeList
from main_store.models import Items, User


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "fetrisa_toy.settings")
django.setup()


# class BucketCreateViewTestCase(TestCase):
#     def setUp(self):
#         self.client = APIClient()
#
#     def test_bucket_create_view(self):
#         url = reverse("bucket-create")
#         data = {"name": "Test Bucket", "user_id": 1}
#         response = self.client.post(url, data)
#
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(response.json(), {"success": True})


class BuketListViewTestCase(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()

    def test_buket_list_view(self):
        url = reverse("buket-user-list", kwargs={"user_id": 1})
        request = self.factory.get(url)
        response = BuketList.as_view()(request, user_id=1)

        self.assertEqual(response.status_code, status.HTTP_200_OK)


# class LikeCreateViewTestCase(TestCase):
#     def setUp(self):
#         self.client = APIClient()
#
#     def test_like_create_view(self):
#         url = reverse("like-create")
#         data = {"user_id": 1, "post_id": 1}
#         response = self.client.post(url, data)
#
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(response.json(), {"success": True})


class LikeListViewTestCase(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()

    def test_like_list_view(self):
        url = reverse("like-user-list", kwargs={"user_id": 1})
        request = self.factory.get(url)
        response = LikeList.as_view()(request, user_id=1)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
