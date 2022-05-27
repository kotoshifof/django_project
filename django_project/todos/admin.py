from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from .models import Todo


class TodoAdmin(admin.ModelAdmin):
    list_display = ('name', 'completed', 'created_at', 'updated_at',)


admin.site.register(Todo)
