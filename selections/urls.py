from django.urls import path

from selections import views

urlpatterns = [
    path('', views.SelectionListView.as_view()),
    path('post/', views.SelectionCreateView.as_view()),
    path('<int:pk>/', views.SelectionDetailView.as_view()),
    path('<int:pk>/update/', views.SelectionUpdateView.as_view()),
    path('<int:pk>/delete/', views.SelectionDeleteView.as_view()),
]
