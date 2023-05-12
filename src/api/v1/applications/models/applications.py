from uuid import uuid4

from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Application(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid4,
        editable=False  # To prevent editing in admin panel
    )
    user = models.ForeignKey(
        to=User,
        null=True,
        on_delete=models.SET_NULL,
        related_name="applications"
    )
    job = models.ForeignKey(
        to="applications.Job",
        null=True,
        on_delete=models.SET_NULL,
        related_name="applications"
    )

    class Meta:
        db_table = "applications"
        # User can apply to multiple jobs
        # but every application should be attached only to one job
        unique_together = ("user", "job")
