from rest_framework import viewsets, mixins
from wallet.models import Record
from wallet.serializers import RecordSerializer
from wallet.serializers import UserSerializer
from django.utils.decorators import method_decorator
from rest_framework.decorators import action, api_view, permission_classes
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema, no_body
import rest_framework.status as status
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication


class UserViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.all()

    def list(self, request):
        users = self.get_queryset()
        serializer = self.get_serializer(users, many=True)
        return Response(serializer.data) 

    def retrieve(self, request, token=None):
        user = self.get_object()
        serializer = self.get_serializer(user)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        saved = serializer.save()

        headers = self.get_success_headers(serializer.data)
        serializer = UserSerializer(saved)
        return Response(
            serializer.data, status.HTTP_201_CREATED, headers=headers
        )

        serializer_class = UserSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status.HTTP_204_NO_CONTENT)
        