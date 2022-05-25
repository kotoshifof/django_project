from os import environ
import pytest
from django.conf import settings
from django.contrib.auth.models import AnonymousUser
from django.http import HttpRequest, HttpResponseRedirect
from django.test import RequestFactory
from django.urls import reverse
import requests

from django_project.users.models import User
from django_project.users.tests.factories import UserFactory
from django_project.weather.tests.factories import CityFactory
from django_project.weather.views import weather_index_view

pytestmark = pytest.mark.django_db

WEATHER_API_KEY = environ.get('WEATHER_API_KEY')


class TestCityIndexView:

    # HACK 必要？ここでテストするべきか？
    def test_weather_api(self):
        r = requests.get(f'http://api.weatherapi.com/v1/current.json?key={WEATHER_API_KEY}&q=London')
        assert r.status_code == 200

    def test_authenticated(self, user: User, rf: RequestFactory):
        request = rf.get("/fake-url/")
        request.user = UserFactory()

        response = weather_index_view(request)

        assert response.status_code == 200

    def test_not_authenticated(self, user: User, rf: RequestFactory):
        request = rf.get("/fake-url/")
        request.user = AnonymousUser()

        response = weather_index_view(request)
        login_url = reverse(settings.LOGIN_URL)

        assert isinstance(response, HttpResponseRedirect)
        assert response.status_code == 302
        assert response.url == f"{login_url}?next=/fake-url/"

    def test_authenticated(self, user: User, rf: RequestFactory):
        request = rf.get("/fake-url/")
        weather = CityFactory()

        response = weather_index_view(request)

        assert response.status_code == 201
