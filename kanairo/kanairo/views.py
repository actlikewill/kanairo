from rest_framework.decorators import api_view
from rest_framework.response import Response 
from rest_framework import status, generics, permissions
from datetime import datetime

@api_view(['GET'])
def index(request):
    date = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    message = 'Server is live current time is '
    return Response(data=message + date, status=status.HTTP_200_OK)

class ProtectedView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return Response({"hello": "there"})