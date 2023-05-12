# Generated by Django 4.2.1 on 2023-05-12 09:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('type', models.CharField(choices=[('PT', 'part-time'), ('FT', 'full-time')], default='FT', max_length=2)),
            ],
            options={
                'db_table': 'jobs',
            },
        ),
        migrations.CreateModel(
            name='JobHeader',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('rich_title_text', models.TextField()),
                ('rich_subtitle_text', models.TextField()),
                ('job', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='header', to='applications.job')),
            ],
            options={
                'db_table': 'job_headers',
            },
        ),
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('job', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='applications', to='applications.job')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='applications', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'applications',
                'unique_together': {('user', 'job')},
            },
        ),
    ]