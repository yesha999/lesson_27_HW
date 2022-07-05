from django.urls import path
from ads.views import ad_views, cat_views

# Для АД
urlpatterns = [
    path('ad/', ad_views.AdListView.as_view()),
    path('ad/post/', ad_views.AdCreateView.as_view()),
    path('ad/<int:pk>/', ad_views.AdDetailView.as_view()),
    path('ad/<int:pk>/update/', ad_views.AdUpdateView.as_view()),
    path('ad/<int:pk>/delete/', ad_views.AdDeleteView.as_view()),
    path('ad/<int:pk>/upload_image/', ad_views.AdImageView.as_view()),
]

# Для Categories
urlpatterns += [path('cat/', cat_views.CatListView.as_view()),
                path('cat/post/', cat_views.CatCreateView.as_view()),
                path('cat/<int:pk>/', cat_views.CatDetailView.as_view()),
                path('cat/<int:pk>/update/', cat_views.CatUpdateView.as_view()),
                path('cat/<int:pk>/delete/', cat_views.CatDeleteView.as_view()),
                ]

# Для Users
urlpatterns += []

# Для Locations
urlpatterns += []
