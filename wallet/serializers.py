from rest_framework import serializers
from .models import IAMUser, Record

class IAMUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = IAMUser
        fields = ['uuid', 'username']

class RecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Record
        fields = ['uuid', 'user', 'amount', 'date', 'description']
        