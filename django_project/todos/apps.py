from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class TodosConfig(AppConfig):
    name = "django_project.todos"
    verbose_name = _("Todos")

    def ready(self):
        try:
            import django_project.todos.signals  # noqa F401
        except ImportError:
            pass
