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

    def get_balance_single_info(self, user_id, category_id, year, month): #budget, spent
        try:
            budget = Budget.objects.get(category_id=category_id, user_id=user_id, date_month=month, date_year=year)
        except Budget.DoesNotExist:
            return False, None, None    
        budget = budget.budget

        related_records = Record.objects.filter(user_id=user_id, category_id=category_id, date__year=year, date__month=month).values()
        spent = 0
        for record in related_records:
            spent += record['amount']
        return True, budget, spent 

    def list(self, request):
        user = request.user 
        print(request.body)
        data_json = json.loads(request.body)
        month, year = data_json['month'], data_json['year']
        categories = Category.objects.all()
        ret = []
        for category in categories:
            is_exist, budget, spent = self.get_balance_single_info(user.id, category.id, year, month)
            if is_exist:
                ret.append({'category': category.name, 'budget': budget, 'spent': spent})
        return Response(ret)


        