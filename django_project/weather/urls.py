
from django.urls import path

from django_project.weather.views import weather_index_view

app_name = "weather"
urlpatterns = [
    path("", view=weather_index_view, name="index"),
]
