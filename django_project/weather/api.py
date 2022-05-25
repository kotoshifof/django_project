from os import environ
from django import forms
import requests

from django_project.weather.models import City


WEATHER_API_KEY = environ.get('WEATHER_API_KEY')


def get_request_weather_data(city: str) -> requests.Response:
    return requests.get(
        f'http://api.weatherapi.com/v1/current.json?key={WEATHER_API_KEY}&q={city}')
