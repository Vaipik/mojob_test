from django.contrib.auth import get_user_model
import factory.fuzzy

from ..models import Application
from .jobs import JobFactory


User = get_user_model()


class UserFactory(factory.django.DjangoModelFactory):
    """This is factory is here beacuse we don't have auth applications
    this is the only model that requires user in this project"""
    username = "test_username_test"  # if new username required call factory as UserFactory(username="new_username")
    password = factory.PostGenerationMethodCall('set_password', 'password')

    class Meta:
        model = User
        django_get_or_create = ('username', )


class ApplicationFactory(factory.django.DjangoModelFactory):
    job = factory.SubFactory(JobFactory)
    user = factory.SubFactory(UserFactory)

    class Meta:
        model = Application
