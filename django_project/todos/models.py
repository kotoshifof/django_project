from django_project.users.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _
from bpmappers.djangomodel import ModelMapper


class Todo(models.Model):
    class Meta:
        db_table = 'todo'
        verbose_name = 'Todo'
    name = models.CharField(_("name"), max_length=80)
    completed = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class TodoMapper(ModelMapper):
    class Meta:
        model = Todo
