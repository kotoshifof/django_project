from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from .models import City


class CityAdmin(admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(City)
