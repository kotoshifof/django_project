from django.db import models
from django.db.models import CharField
from django.forms import BooleanField
from django.utils.translation import gettext_lazy as _

from django_project.users.models import User


class Todo(models.Model):
    class Meta:
        db_table = 'todo'
        verbose_name = 'Todo'
    name = CharField(_("name"), max_length=80)
    completed = BooleanField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
