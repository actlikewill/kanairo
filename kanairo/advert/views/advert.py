from rest_framework import generics, permissions
from user.permissions import IsOwnerOrReadOnly
from ..serializers.advert import AdvertSerializer

from django.shortcuts import get_object_or_404
from ..models.advert import Advert


class AdvertListCreateView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = AdvertSerializer    

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):        
        tags = self.request.query_params.getlist('tags', None)       
        if tags is not None: 
            return Advert.objects.filter(tags__name__in=tags)
        return Advert.objects.all()

        
class AdvertRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]    
    serializer_class = AdvertSerializer
    queryset = Advert.objects.all()
    