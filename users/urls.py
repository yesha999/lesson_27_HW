from django.urls import path
from rest_framework import routers

from users import views

urlpatterns = [
    path('users/', views.UserListView.as_view()),
    path('users/post/', views.UserCreateView.as_view()),
    path('users/<int:pk>/', views.UserDetailView.as_view()),
    path('users/<int:pk>/update/', views.UserUpdateView.as_view()),
    path('users/<int:pk>/delete/', views.UserDeleteView.as_view()),
]


location_router = routers.SimpleRouter()
location_router.register('location', views.LocationViewSet)

urlpatterns += location_router.urls