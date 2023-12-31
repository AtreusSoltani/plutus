from django.urls import path, include
from rest_framework import routers
from wallet.views import (
    user,
    record,
    auth,
    category,
    budget,
    token,
    report
)


router = routers.DefaultRouter()
router.register(r'users', user.UserViewSet, basename='users')
router.register(r'records', record.RecordViewSet, basename='records')
router.register(r'categories', category.CategoryViewSet, basename='categories')
router.register(r'budget', budget.BudgetViewSet, basename='budget')
router.register(r'token', token.TokenViewSet, basename='token')
router.register(r'login', auth.LoginViewset, basename='login')
router.register(r'register', auth.RegisterViewset, basename='register')
#router.register(r'report', auth.RegisterViewset, basename='register')

# router.register(r'register', auth.RegistrationViewSet, basename='register')
# router.register(r'login', MyObtainTokenPairView.as_view(), name='login')

urlpatterns = [
    path('', include(router.urls)),
    path('report/category/<int:year>', report.ReportViewSet.as_view({'get': 'get_categories_expend'}), name='get_categories_expend'),
    path('report/expend/<int:year>', report.ReportViewSet.as_view({'get': 'get_months_expend'}), name='get_months_expend'),
    path('report/inventory/<int:year>', report.ReportViewSet.as_view({'get': 'get_months_inventory'}), name='get_months_inventory'),
]