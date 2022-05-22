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
        cities = user.city_set.all()

        # userに結び付けられたnameをもとに天気情報を取得する
        weather_data_list = []
        for city in cities:
            r = requests.get(
                f'http://api.weatherapi.com/v1/current.json?key={WEATHER_API_KEY}&q={city.name}')
            weather_data_list.append(r.json())

        context = {
            'weather_data_list': weather_data_list,
        }
        template_name: str = "weather/weather_index.html"
        return TemplateResponse(request, template_name, context)


weather_index_view = WeatherIndexView.as_view()
