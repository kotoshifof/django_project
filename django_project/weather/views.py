from os import environ
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.translation import gettext_lazy as _
from django.views.generic import View
from django.template.response import TemplateResponse
import requests

User = get_user_model()
WEATHER_API_KEY = environ.get('WEATHER_API_KEY')


class WeatherIndexView(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        user = User.objects.get(pk=request.user.id)
        weather_list = user.weather_set.all()

        # userに結び付けられたcityをもとに天気情報を取得する
        weather_info_list = []
        for weather in weather_list:
            r = requests.get(
                f'http://api.weatherapi.com/v1/current.json?key={WEATHER_API_KEY}&q={weather.city}')
            weather_info_list.append(r.json())

        context = {
            'weather_info_list': weather_info_list,
        }
        template_name: str = "weather/weather_index.html"
        return TemplateResponse(request, template_name, context)


weather_index_view = WeatherIndexView.as_view()
