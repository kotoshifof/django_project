from django.db import models
from django.db.models import CharField
from django.utils.translation import gettext_lazy as _

from django_project.users.models import User


class City(models.Model):
    class Meta:
        db_table = 'city'
        verbose_name = '都市'

    def __str__(self):
        return self.name
    name = CharField(_("name"), max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
