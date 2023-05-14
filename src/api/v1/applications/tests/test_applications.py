from django.urls import reverse
from rest_framework.test import APITestCase

from ..factories import ApplicationFactory, UserFactory, JobHeaderFactory


class ApplicationTest(APITestCase):

    @classmethod
    def setUpTestData(cls):
        password = "123123ASAS!!@(SA"
        user = UserFactory(password=password)
        cls.list_url = reverse(f"applications:user_applications_list", kwargs={"pk": user.id})
        cls.credentials = {
            "username": user.username,
            "password": password
        }
        cls.user_applications = [ApplicationFactory(user=user) for _ in range(10)]

    def test_get_applications_list_authorized(self):
        self.client.login(**self.credentials)
        response = self.client.get(self.list_url)
        response_json = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response_json, list)  # response is a list
        self.assertEqual(len(response_json), 10)

    def test_get_applications_list_unauthorized(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, 403)

