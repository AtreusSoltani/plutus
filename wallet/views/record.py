from rest_framework import viewsets, mixins
from wallet.models import IAMUser, Record
from wallet.serializers import IAMUserSerializer, RecordSerializer
from django.utils.decorators import method_decorator
from rest_framework.decorators import action, api_view, permission_classes
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema, no_body
import rest_framework.status as status

@method_decorator(
    name="list",
    decorator=swagger_auto_schema(
        operation_description="Lists all records",
        tags=["Records"],
    ),
)
@method_decorator(
    name="retrieve",
    decorator=swagger_auto_schema(
        operation_description="Gets the record with the given uuid",
        tags=["Records"],
    ),
)
class RecordViewSet(viewsets.ModelViewSet):
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
        serializer = RecordSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        saved = serializer.save()

        headers = self.get_success_headers(serializer.data)
        serializer = RecordSerializer(saved)
        return Response(
            serializer.data, status.HTTP_201_CREATED, headers=headers
        )

        serializer_class = UserSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(HTTP_204_NO_CONTENT)