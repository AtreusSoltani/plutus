from rest_framework import viewsets, mixins
from wallet.models import Record, Category
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
        user = request.user
        try:
            start_date = request.query_params['start_date']
        except:
            start_date = '1970-01-01'
        try:
            end_date = request.query_params['end_date']
        except:
            end_date = '9999-12-31'
        try:
            category = [request.query_params['category']]
        except:
            category = Category.objects.all().values_list('name', flat=True)

        records = Record.objects.filter(user_id=user.id, date__range=[start_date, end_date], category__in=category)
        serializer = self.get_serializer(records, many=True)
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
        