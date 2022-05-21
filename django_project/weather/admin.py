from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from .models import Weather


class WeatherAdmin(admin.ModelAdmin):
    list_display = ('city',)


admin.site.register(Weather)
