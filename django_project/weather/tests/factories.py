from typing import Any, Sequence

from django.contrib.auth import get_user_model
from factory import Faker, post_generation
from factory.django import DjangoModelFactory

from django_project.users.tests.factories import UserFactory


class CityFactory(DjangoModelFactory):

    name = Faker("name")
    user = UserFactory()

    # @post_generation
    # def password(self, create: bool, extracted: Sequence[Any], **kwargs):
    #     password = (
    #         extracted
    #         if extracted
    #         else Faker(
    #             "password",
    #             length=42,
    #             special_chars=True,
    #             digits=True,
    #             upper_case=True,
    #             lower_case=True,
    #         ).evaluate(None, None, extra={"locale": None})
    #     )
    #     self.set_password(password)

    # class Meta:
    #     model = get_user_model()
    #     django_get_or_create = ["username"]