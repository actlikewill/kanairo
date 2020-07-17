from rest_framework import generics, permissions
from ..models.category import Category
from ..serializers.category import CategorySerializer

class CategoryListAPIView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    
