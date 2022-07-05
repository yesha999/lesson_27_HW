from django.contrib import admin

from ads.models import *


admin.site.register(AdsModel)
admin.site.register(CategoriesModel)
admin.site.register(UserModel)
admin.site.register(LocationModel)

