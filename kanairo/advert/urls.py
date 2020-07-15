from django.urls import path
from .views import AdvertListCreateView, AdvertRetrieveUpdateDestroyView

urlpatterns = [
    path('', AdvertListCreateView.as_view()),
    path('<int:pk>', AdvertRetrieveUpdateDestroyView.as_view()),

]