from django.urls import path, include
from rest_framework.routers import SimpleRouter

from ..applications.views import JobViewSet, UserApplicationGet


job_router = SimpleRouter()
job_router.register(prefix="jobs", viewset=JobViewSet, basename="job")


urlpatterns = [
    path("", include(job_router.urls)),
    path(
        r"users/<int:pk>/applications/", UserApplicationGet.as_view(), name="user_applications_list")
]
