from django.utils.translation import gettext_lazy as _
from django.apps import AppConfig


# class CityConfig(AppConfig):
#     default_auto_field = 'django.db.models.BigAutoField'
#     name = 'city'


class CityConfig(AppConfig):
    name = "django_project.weather"
    verbose_name = _("City")

    def ready(self):
        try:
            import django_project.weather.signals  # noqa F401
        except ImportError:
            pass
