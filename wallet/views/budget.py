from rest_framework import viewsets, mixins
from wallet.models import Budget, Record, Category
from wallet.serializers import BudgetSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
import json
from rest_framework.response import Response

class BudgetViewSet(viewsets.ModelViewSet):
    queryset = Budget.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = BudgetSerializer

    def get_balance_single_info(self, user_id, category, year, month): #budget, spent
        try:
            budgetObject = Budget.objects.get(category=category, user_id=user_id, date_month=month, date_year=year)
            budget = budgetObject.budget
        except Budget.DoesNotExist:
            budget = 0

        related_records = Record.objects.filter(user_id=user_id, category=category, date__year=year, date__month=month).values()
        spent = 0
        for record in related_records:
            spent += record['amount']
        return True, budget, spent 

    def list(self, request):
        user = request.user
        month, year = request.query_params['month'], request.query_params['year']
        print(f'{month}, {year}')
        categories = Category.objects.all()
        ret = []
        for category in categories:
            is_exist, budget, spent = self.get_balance_single_info(user.id, category.name, year, month)
            if is_exist:
                ret.append({'category': category.name, 'budget': budget, 'spent': spent})
        return Response(ret)


        