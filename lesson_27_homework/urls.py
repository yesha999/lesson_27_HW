from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from ads.views.ad_views import StartView

urlpatterns = [path('admin/', admin.site.urls),
               path('', StartView.as_view()),
               path('', include("ads.urls")),
               path('users/', include("users.urls")),
               ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
