from django.db import models
from users.models import User, Location
from django.core import validators


class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    slug = models.CharField(unique=True, max_length=10, validators=[validators.MinLengthValidator(5)])

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Ad(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, validators=[validators.MinLengthValidator(10)])
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    price = models.IntegerField(validators=[validators.MinValueValidator(0)])
    description = models.CharField(max_length=2000, null=True, blank=True)
    is_published = models.BooleanField(default=False)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = "Объявление"
        verbose_name_plural = "Объявления"
