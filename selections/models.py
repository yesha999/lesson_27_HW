from django.contrib.auth.models import AbstractUser
from django.db import models

from ads.models import Ad
from users.models import User


class Selection(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    items = models.ManyToManyField(Ad)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Подборка"
        verbose_name_plural = "Подборки"