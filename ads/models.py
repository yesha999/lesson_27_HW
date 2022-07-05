from django.db import models
from users.models import UserModel, LocationModel


class CategoriesModel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class AdsModel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    author = models.ForeignKey(UserModel, on_delete=models.CASCADE, null=True, blank=True)
    price = models.IntegerField()
    description = models.CharField(max_length=2000, null=True, blank=True)
    is_published = models.BooleanField(default=False)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    category = models.ForeignKey(CategoriesModel, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = "Объявление"
        verbose_name_plural = "Объявления"
