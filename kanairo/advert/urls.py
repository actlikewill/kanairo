from django.urls import path
from .views.advert import AdvertListView, AdvertCreateView, AdvertRetrieveUpdateDestroyView
from .views.categories import CategoryListAPIView

urlpatterns = [
    path('', AdvertListView.as_view()),
    path('create/', AdvertCreateView.as_view()),
    path('<int:pk>', AdvertRetrieveUpdateDestroyView.as_view()),
    path('categories/', CategoryListAPIView.as_view()),

]