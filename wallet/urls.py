from django.urls import path, include
from rest_framework import routers
from wallet.views import (
    user,
    record,
    auth,
)


router = routers.DefaultRouter()
router.register(r'users', user.UserViewSet, basename='users')
router.register(r'records', record.RecordViewSet, basename='records')
# router.register(r'register', auth.RegistrationViewSet, basename='register')
# router.register(r'login', MyObtainTokenPairView.as_view(), name='login')

urlpatterns = [
    path('', include(router.urls)),
]