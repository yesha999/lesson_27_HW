from datetime import date

from dateutil.relativedelta import relativedelta
from django.contrib.auth.models import AbstractUser
from django.db import models
from rest_framework.exceptions import ValidationError


def check_birth_date(value: date, MINIMAL_USER_AGE=9):
    difference_in_years = relativedelta(date.today(), value).years
    if difference_in_years < MINIMAL_USER_AGE:  # Минимальный возраст
        raise ValidationError(f"Запрещено регистрироваться пользователям младше {MINIMAL_USER_AGE} лет.")


def check_rambler_email(value: str):
    if value.endswith('rambler.ru'):
        raise ValidationError(f"Запрещено регистрироваться пользователям с почтового адреса в домене rambler.ru")


class Location(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    lat = models.DecimalField(max_digits=8, decimal_places=6, null=True, blank=True)
    lng = models.DecimalField(max_digits=8, decimal_places=6, null=True, blank=True)

    class Meta:
        verbose_name = "Локация"
        verbose_name_plural = "Локации"


class User(AbstractUser):
    ROLES = [('member', 'Участник'), ('admin', 'Админ'),
             ('moderator', 'Модератор')]
    role = models.CharField(max_length=9, choices=ROLES, default='member')
    location = models.ManyToManyField(Location)
    birth_date = models.DateField(validators=[check_birth_date])
    email = models.EmailField(unique=True, validators=[check_rambler_email])

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
