from rest_framework import viewsets, mixins
from wallet.models import Record
from wallet.serializers import RecordSerializer
from django.utils.decorators import method_decorator
from rest_framework.decorators import action, api_view, permission_classes
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema, no_body
import rest_framework.status as status
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

class RecordViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = RecordSerializer

    def get_queryset(self):
        return Record.objects.all()

    def list(self, request):
        records = self.get_queryset()
        serializer = self.get_serializer(records, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        record = self.get_object()
        serializer = self.get_serializer(record)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        print(request.user.id)
        serializer = RecordSerializer(data={**request.data,'user_id':request.user.id})
        serializer.is_valid(raise_exception=True)
        saved = serializer.save()

        headers = self.get_success_headers(serializer.data)
        serializer = RecordSerializer(saved)
        return Response(
            serializer.data, status.HTTP_201_CREATED, headers=headers
        )
        