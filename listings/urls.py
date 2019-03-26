from django.urls import path
from . import views

urlpatterns = [
    path('', views.listings, name="listings"),
    path('<int:listing_id>/listing/', views.listing, name="listing"),
    path('search/', views.search, name="search"),
]