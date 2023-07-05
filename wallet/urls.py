from django.urls import path, include
from rest_framework import routers
from wallet.views import (
    user,
    record,
)


router = routers.DefaultRouter()
router.register(r'users', user.IAMUserViewSet, basename='users')
router.register(r'records', record.RecordViewSet, basename='records')

urlpatterns = [
    path('', include(router.urls)),
]

# urlpatterns = [
#     path('users/', user.IAMUserViewSet.as_view({"get": "list", "post": "create", "delete": "destroy"})),
#     # path('users/<uuid:user_uuid>/', user.IAMUserDetail.as_view()),
#     path('records/', record.RecordViewSet.as_view({"get": "list"})),
#     # path('users/<uuid:user_uuid>/records/<uuid:record_uuid>/', RecordDetails.as_view())
# ]