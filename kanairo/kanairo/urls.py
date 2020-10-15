"""The main urls are here. """
from django.contrib import admin
from django.urls import path, include
from .views import index, ProtectedView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('checkserverstatus/', index, name='index'),
    path('protected/', ProtectedView.as_view()),
    path('auth/', include('users.urls')),
    path('advert/', include('advert.urls'))
]