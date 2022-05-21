from django.db import models
from django.db.models import CharField
from django.utils.translation import gettext_lazy as _

from django_project.users.models import User


class Weather(models.Model):
    # class Meta:
    #     db_table = 'weather'
    #     verbose_name = verbose_name_plural = '天気'
    city = CharField(_("City"), max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
