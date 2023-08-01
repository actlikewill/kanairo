from django.urls import path

from . import views

urlpatterns = [
    path("ad/", views.AdvertListView.as_view(), name="advert_list"),
    path("ad/<slug>/", views.AdvertDetailView.as_view(), name="advert_detail"),
]
