"""The main urls are here. """
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("kanairo.urls")),
]
