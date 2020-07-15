from rest_framework import serializers
from .models import Advert
from user.serializers import UserPublicSerializer

class AdvertSerializer(serializers.ModelSerializer):
    user        = UserPublicSerializer(read_only=True)
    class Meta:
        model = Advert
        fields = [
            'id',
            'user',
            'title',
            'description',
            'image',
            'timestamp',
        ]
        read_only_fields = ['user']
