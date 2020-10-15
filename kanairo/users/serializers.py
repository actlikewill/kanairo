from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class UserPublicSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'email'
        ]
        
class SocialSerializer(serializers.Serializer):
    """
    Serializer which accepts an OAuth2 access token and provider.
    """
    provider = serializers.CharField(max_length=255, required=True)
    access_token = serializers.CharField(max_length=4096, required=True, trim_whitespace=True)