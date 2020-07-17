from rest_framework import serializers
from ..models.advert import Advert
from ..models.category import Category
from user.serializers import UserPublicSerializer

class AdvertSerializer(serializers.ModelSerializer):
    user        = UserPublicSerializer(read_only=True)    
    ad_category = serializers.SerializerMethodField(read_only=True)   
    class Meta:
        model = Advert
        fields = [
            'id',
            'user',
            'title',
            'category',
            'ad_category',
            'description',
            'image',
            'timestamp',
        ]
        read_only_fields = ['user']
        extra_kwargs = {'category': {'write_only': True}}

    def get_ad_category(self, obj):
        category = Category.objects.get(pk=obj.category.id)
        ad_category = {
            "id": category.id,
            "category": category.title
        }        
        return ad_category
