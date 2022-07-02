from django.db import models


class AdsModel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.CharField(max_length=2000, null=True, blank=True)
    address = models.CharField(max_length=2000)
    is_published = models.BooleanField(default=False)


class CategoriesModel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)


