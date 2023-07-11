from rest_framework import viewsets, mixins
from wallet.models import Category
from wallet.serializers import CategorySerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = CategorySerializer

        