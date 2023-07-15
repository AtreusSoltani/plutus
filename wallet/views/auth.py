from rest_framework import viewsets, mixins
from rest_framework.decorators import permission_classes
from rest_framework import viewsets, permissions
import json 
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
# class MyObtainTokenPairView(TokenObtainPairView):
#     permission_classes = (AllowAny,)
#     serializer_class = MyTokenObtainPairSerializer


"""def login(request):
    if request.method != 'POST':
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
    user_infos = json.loads(request.body)
    user_name, password = user_infos['username'], user_infos['password']
    user = User.objects.get(username=user_name)
    if user['password'] != password:
        return Response(data={'message': "username or password is wrong. please try again"}, status=status.HTTP_401_UNAUTHORIZED)
    token = Token.objects.create(user=user['id'])
    return Response(data={'token':f'{token.key}'}, status=status.HTTP_200_OK)

def sign_up(request):
    if request.method != 'POST':
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
    user_infos = json.loads(request.body)
    user_name, password = user_infos['username'], user_infos['password']
    
    user = User.objects.get(username=user_name)
    if user['password'] != password:
        return Response(data={'message': "username or password is wrong. please try again"}, status=status.HTTP_401_UNAUTHORIZED)
    token = Token.objects.create(user=user['id'])
    return Response(data={'token':f'{token.key}'}, status=status.HTTP_200_OK)"""


class LoginViewset(viewsets.ModelViewSet):
    permission_classes = [
        permissions.AllowAny
    ]

    def create(self, request, *args, **kwargs):
        if request.method != 'POST':
          return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        user_infos = json.loads(request.body)
        user_name, password = user_infos['username'], user_infos['password']
        user = User.objects.get(username=user_name)
        print(user)
        if user.password != password:
            return Response(data={'message': "username or password is wrong. please try again"}, status=status.HTTP_401_UNAUTHORIZED)
        token = Token.objects.create(user=user)
        print(token.key)
        return Response(data={'token':f'{token.key}'}, status=status.HTTP_200_OK)
    

class RegisterViewset(viewsets.ModelViewSet):
    permission_classes = [
        permissions.AllowAny
    ]

    def create(self, request, *args, **kwargs):
        user_infos = json.loads(request.body)
        user_name, password = user_infos['username'], user_infos['password']

        def user_is_exist() -> bool:
            objs = User.objects.filter(username=user_name)
            print(len(objs))
            return len(list(objs)) > 0
        
        if not user_is_exist():
            new_user = User(username=user_name, password=password)
            new_user.save()
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(data={'message':'user with this username is already exist.'}, status=status.HTTP_401_UNAUTHORIZED)
