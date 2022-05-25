from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import View
from django.template.response import TemplateResponse
from django_project.weather.api import get_request_weather_data
from django_project.weather.forms import CreateCityForm

from django_project.weather.models import City

User = get_user_model()


# userに結び付けられたcity.nameをもとに天気情報を取得する
def get_weather_data_list(cities: list[City]) -> list:
    weather_data_list = []
    for city in cities:
        r = get_request_weather_data(city.name)
        weather_data_list.append(r.json())
    return weather_data_list


class WeatherIndexView(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        form = CreateCityForm()
        cities = request.user.city_set.all()

        weather_data_list = get_weather_data_list(cities)

        context = {
            'weather_data_list': weather_data_list,
            'form': form,
        }
        template_name: str = "weather/weather_index.html"
        return TemplateResponse(request, template_name, context)

    def post(self, request, *args, **kwargs):
        if 'city' in request.POST:
            return self.delete(request)

        form = CreateCityForm(request.POST)
        template_name: str = "weather/weather_index.html"

        if not form.is_valid():
            cities = request.user.city_set.all()
            weather_data_list = get_weather_data_list(cities)
            context = {
                'weather_data_list': weather_data_list,
                'form': form,
            }
            return TemplateResponse(request, template_name, context)

        city = form.save(commit=False)
        # HACK Userは同じcity.nameを登録できないようしているが、コードが冗長
        if request.user.city_set.filter(name=city.name).exists():
            form.add_error('name',
                           forms.ValidationError('すでに登録されています'))
            cities = request.user.city_set.all()
            weather_data_list = get_weather_data_list(cities)
            context = {
                'weather_data_list': weather_data_list,
                'form': form,
            }
            return TemplateResponse(request, template_name, context)

        city.user_id = request.user.id
        city.save()
        messages.info(request, f"{city.name}を登録しました")

        return HttpResponseRedirect(reverse('weather:index'))

    def delete(self, request,):
        city = request.POST['city']
        request.user.city_set.filter(name=city).delete()
        messages.error(request, f"{city}の登録を解除しました")
        return HttpResponseRedirect(reverse('weather:index'))


weather_index_view = WeatherIndexView.as_view()
