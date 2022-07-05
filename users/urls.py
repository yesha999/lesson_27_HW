from django.urls import path
from users import views

urlpatterns = [
    path('user/', views.UserListView.as_view()),
    path('user/post/', views.UserCreateView.as_view()),
    path('user/<int:pk>/', views.UserDetailView.as_view()),
    path('user/<int:pk>/update/', views.UserUpdateView.as_view()),
    path('user/<int:pk>/delete/', views.UserDeleteView.as_view()),
]