import json
from rest_framework.views import APIView
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import SocialSerializer, UserPublicSerializer


class SocialLoginView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = SocialSerializer

    def get(self, request):
        user = self.request.user
        token = RefreshToken.for_user(user)
        user_details = UserPublicSerializer(user)
        print(token.access_token)
        return Response({"user": user_details.data, "refresh" : str(token), "access": str(token.access_token)})

