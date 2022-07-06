from django.contrib import admin

from users.models import UserModel, LocationModel

admin.site.register(UserModel)
admin.site.register(LocationModel)
