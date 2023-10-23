from rest_framework import viewsets, mixins
from rest_framework.decorators import permission_classes
from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from wallet.models import Budget, Record, Category
from rest_framework.throttling import UserRateThrottle

class   ReportViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    throttle_classes = [UserRateThrottle]

    
    @action(detail=True, methods=['get'])
    def get_categories_expend(self, request, year):
        user = request.user 
        related_records = Record.objects.filter(user_id=user.id, date__year=year)
        category = set([x.category for x in related_records])
        def get_expense_for_category(cat):
            return sum([x.amount for x in related_records if x.category == cat and x.amount < 0])
        ret = dict([(cat.name, get_expense_for_category(cat)) for cat in category])
        return Response(ret, status.HTTP_200_OK)

    @action(detail=True, methods=['get'])
    def get_months_expend(self, request, year):
        user = request.user
        related_records = Record.objects.filter(user_id=user.id, date__year=year)
        def get_month_expend(month):
            return sum([x.amount for x in related_records if x.date.month == month and x.amount < 0])
        ret = dict([(month, get_month_expend(month)) for month in range(1,13)])
        return Response(ret, status.HTTP_200_OK)

    @action(detail=True, methods=['get'])
    def get_months_inventory(self, request, year):
        user = request.user
        related_records = Record.objects.filter(user_id=user.id, date__year=year)
        def get_month_inventory(month):
            return sum([x.amount for x in related_records if x.date.month == month])
        ret = dict([(month, get_month_inventory(month)) for month in range(1,13)])
        return Response(ret, status.HTTP_200_OK)

