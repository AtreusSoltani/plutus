from rest_framework import serializers
from .models import Record, Category, Budget
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "password"]

class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

class RecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Record
        fields = "__all__"

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

class BudgetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Budget
        fields = "__all__"

    def validate(self, attrs):
        month = int(attrs['date_month'])
        if month < 0 or 11 < month:
            raise serializers.ValidationError(f"unexpected month id. the month id is {month}")
        return super().validate(attrs)
