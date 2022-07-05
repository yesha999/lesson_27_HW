from django.db import models


class LocationModel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    lat = models.DecimalField(max_digits=8, decimal_places=6, null=True, blank=True)
    lng = models.DecimalField(max_digits=8, decimal_places=6, null=True, blank=True)

    class Meta:
        verbose_name = "Локация"
        verbose_name_plural = "Локации"


class UserModel(models.Model):
    ROLES = [('member', 'Участник'), ('admin', 'Админ'),
             ('moderator', 'Модератор')]
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    user_name = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    role = models.CharField(max_length=9, choices=ROLES, default='member')
    age = models.PositiveSmallIntegerField()
    location = models.ForeignKey(LocationModel, on_delete=models.SET_NULL,
                                 null=True, blank=True)

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
