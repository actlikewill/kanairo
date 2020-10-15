from django.urls import path, include
from .views import SocialLoginView

urlpatterns = [
    path('', include('djoser.urls')),
    path('', include('djoser.urls.authtoken')),
    path('', include('djoser.urls.jwt')),
    path('', include('rest_framework_social_oauth2.urls')),
    path('oauth/login/', SocialLoginView.as_view()),
]