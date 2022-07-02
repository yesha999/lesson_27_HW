"""lesson_27_homework URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

import ads.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ads.views.StartView.as_view()),
    path('ad/', ads.views.AdListView.as_view()),
    path('ad/<int:pk>/', ads.views.AdDetailView.as_view()),
    path('cat/', ads.views.CatListView.as_view()),
    path('cat/<int:pk>/', ads.views.CatDetailView.as_view()),
]
