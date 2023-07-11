from rest_framework import viewsets, mixins
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from wallet.serializers import UserSerializer, UserInfoSerializer
from wallet.models import User

class TokenViewSet(viewsets.ViewSet ):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]


    def list(self, request):
        serializer = UserInfoSerializer(request.user)
        return Response(serializer.data)

   
        