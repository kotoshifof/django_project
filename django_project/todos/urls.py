
from django.urls import path

from django_project.todos.views import index

app_name = "todos"
urlpatterns = [
    path("", view=index, name="index"),
]
