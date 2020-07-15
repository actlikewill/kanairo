from rest_framework import generics, permissions
from user.permissions import IsOwnerOrReadOnly
from .serializers import AdvertSerializer
from django.shortcuts import get_object_or_404
from .models import Advert


class AdvertListCreateView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = AdvertSerializer
    queryset = Advert.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class AdvertRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]    
    serializer_class = AdvertSerializer
    queryset = Advert.objects.all()   
    
  