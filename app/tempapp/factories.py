from uuid import uuid4

import factory
import factory.fuzzy
from django.utils import timezone

from tempapp.models import User


class TimestampedModelFactory(factory.django.DjangoModelFactory):

    modified_at = factory.Faker(
        "date_time_between", tzinfo=timezone.utc, start_date="-1m", end_date="now"
    )
    created_at = factory.Faker(
        "date_time_between", tzinfo=timezone.utc, start_date="-2m", end_date="-1m"
    )


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    uuid = factory.LazyAttribute(lambda x: uuid4())
    email = factory.Faker("email")
    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")
    date_joined = factory.Faker(
        "date_time_between", tzinfo=timezone.utc, start_date="-2y", end_date="-1y"
    )
    is_staff = False
    is_active = True

    @factory.lazy_attribute
    def username(self):
        return self.email
