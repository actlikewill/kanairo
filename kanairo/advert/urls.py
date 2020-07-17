from django.urls import path
from .views.advert import AdvertListCreateView, AdvertRetrieveUpdateDestroyView
from .views.categories import CategoryListAPIView

urlpatterns = [
    path('', AdvertListCreateView.as_view()),
    path('<int:pk>', AdvertRetrieveUpdateDestroyView.as_view()),
    path('categories/', CategoryListAPIView.as_view()),

]