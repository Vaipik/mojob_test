import json

from django.urls import reverse
from django.utils.html import strip_tags
from rest_framework.test import APITestCase

from ..factories import UserFactory, JobHeaderFactory
from ..views import JobViewSet
from ..urls import job_router


class JobTest(APITestCase):

    @classmethod
    def setUpTestData(cls):
        cls.job = JobHeaderFactory().job
        basename = job_router.get_default_basename(JobViewSet)
        cls.list_url = reverse(f"applications:{basename}s-list")
        cls.detail_url = reverse(f"applications:{basename}s-detail", kwargs={"pk": cls.job.pk})
        password = "123123ASAS!!@(SA"
        user = UserFactory(password=password)
        cls.credentials = {
            "username": user.username,
            "password": password
        }
        cls.new_job = {
            "name": "TopJob",
            "type": "part-time",
            "header": {
                "rich_title_text": "<i>italic_title</i>",
                "rich_subtitle_text": "<i>italic_subtitle</i>"
            }
        }

    def test_get_jobs_list_authorized(self):
        """Test for access a job-list using GET method if user is authorized"""
        self.client.login(**self.credentials)
        response = self.client.get(self.list_url)
        response_json = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response_json, list)  # response is a list
        self.assertEqual(len(response_json), 1)

    def test_get_jobs_list_unauthorized(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, 403)

    def test_get_detail_jobs_authorized(self):
        self.client.login(**self.credentials)
        response = self.client.get(self.detail_url)
        response_json = response.json()

        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response_json, dict)
        self.assertEqual(len(response_json), 4)
        self.assertEqual(len(response_json["header"]), 4)

    def test_get_detail_jobs_unauthorized(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, 403)

    def test_post_detail_jobs_authorized_success(self):
        self.client.login(**self.credentials)
        response = self.client.post(
            f"{self.list_url}",
            data=json.dumps(self.new_job),
            content_type="application/json"
        )

        self.assertEqual(response.status_code, 201)
        self.assertTrue("plain_title_text" in response.json()["header"])

    def test_post_detail_jobs_unauthorized(self):
        response = self.client.post(
            f"{self.list_url}",
            data=json.dumps(self.new_job),
            content_type="application/json"
        )

        self.assertEqual(response.status_code, 403)

    def test_post_detail_jobs_authorized_wrong_type(self):
        new_job = self.new_job.copy()
        new_job["type"] = "extra-type"
        self.client.login(**self.credentials)
        response = self.client.post(
            f"{self.list_url}",
            data=json.dumps(new_job),
            content_type="application/json"
        )

        self.assertEqual(response.status_code, 400)

    def test_post_detail_jobs_authorized_without_name(self):
        new_job = self.new_job.copy()
        new_job.pop("name")
        self.client.login(**self.credentials)
        response = self.client.post(
            f"{self.list_url}",
            data=json.dumps(new_job),
            content_type="application/json"
        )

        self.assertEqual(response.status_code, 400)

    def test_post_detail_jobs_authorized_without_type(self):
        new_job = self.new_job.copy()
        new_job.pop("type")
        self.client.login(**self.credentials)
        response = self.client.post(
            f"{self.list_url}",
            data=json.dumps(new_job),
            content_type="application/json"
        )

        self.assertEqual(response.status_code, 400)

    def test_post_detail_jobs_authorized_without_header_title_text(self):
        new_job = self.new_job.copy()
        new_job["header"].pop("rich_title_text")
        self.client.login(**self.credentials)
        response = self.client.post(
            f"{self.list_url}",
            data=json.dumps(new_job),
            content_type="application/json"
        )

        self.assertEqual(response.status_code, 400)

    def test_post_detail_jobs_authorized_without_header_subtitle_text(self):
        new_job = self.new_job.copy()
        new_job["header"].pop("rich_subtitle_text")
        self.client.login(**self.credentials)
        response = self.client.post(
            f"{self.list_url}",
            data=json.dumps(new_job),
            content_type="application/json"
        )

        self.assertEqual(response.status_code, 400)

    def test_post_detail_jobs_authorized_without_header(self):
        new_job = self.new_job.copy()
        new_job.pop("header")
        self.client.login(**self.credentials)
        response = self.client.post(
            f"{self.list_url}",
            data=json.dumps(new_job),
            content_type="application/json"
        )

        self.assertEqual(response.status_code, 400)

    def test_put_detail_jobs_authorized(self):
        self.client.login(**self.credentials)
        job = self.new_job.copy()
        job["name"] = "ChangedJobName"
        job["type"] = "full-time"
        job["header"]["rich_title_text"] = r"<h3>rich_TITLE_text</h3>"
        job["header"]["rich_subtitle_text"] = r"<div>rich_SUBTITLE_text</div>"
        response = self.client.put(
            self.detail_url,
            data=json.dumps(job),
            content_type="application/json"
        )
        response_json = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response_json["name"], job["name"])
        self.assertEqual(response_json["type"], job["type"])
        self.assertEqual(response_json["header"]["rich_title_text"], job["header"]["rich_title_text"])
        self.assertEqual(response_json["header"]["rich_subtitle_text"], job["header"]["rich_subtitle_text"])
        self.assertEqual(response_json["header"]["plain_title_text"], strip_tags(job["header"]["rich_title_text"]))

    def test_put_detail_jobs_unauthorized(self):
        response = self.client.put(
            self.detail_url,
            data=json.dumps(self.new_job),
            content_type="application/json"
        )

        self.assertEqual(response.status_code, 403)

    def test_delete_detail_jobs_unauthorized(self):
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, 403)

    def test_delete_detail_jobs_authorized(self):
        self.client.login(**self.credentials)
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, 204)
