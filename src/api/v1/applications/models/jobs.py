from uuid import uuid4

from django.db import models

from .. import constants


class Job(models.Model):
    class JobTypeChoices(models.TextChoices):
        PART_TIME = "PT", "part-time"
        FULL_TIME = "FT", "full-time"

    id = models.UUIDField(
        primary_key=True,
        default=uuid4,
        editable=False  # To prevent editing in admin panel
    )
    name = models.CharField(
        max_length=constants.JOB_NAME_MAX_LENGTH
    )
    type = models.CharField(
        max_length=constants.JOB_TYPE_LENGTH,
        choices=JobTypeChoices.choices,
        default=JobTypeChoices.FULL_TIME  # A huge part of jobs are full-time
    )

    class Meta:
        db_table = "jobs"
        verbose_name = "Job"
        verbose_name_plural = "Jobs"

    def __str__(self) -> str:
        return f"{self.id} | {self.type} | {self.name}"


class JobHeader(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid4,
        editable=False  # To prevent editing in admin panel
    )
    rich_title_text = models.TextField()
    rich_subtitle_text = models.TextField()
    job = models.OneToOneField(
        to="Job",
        on_delete=models.CASCADE,
        related_name="header"  # Attribute for access related model
    )

    class Meta:
        db_table = "job_headers"
        verbose_name = "Job header"
        verbose_name_plural = "Job headers"

    def __str__(self) -> str:
        return f"{self.id} | {self.rich_title_text}, {self.job.name}"
