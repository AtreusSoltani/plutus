from datetime import datetime   
from django.db import models
from django.contrib import admin
import uuid
from django.contrib.auth.models import User
from django import forms

class Category(models.Model):
    name = models.CharField(max_length=100, primary_key=True)

class Budget(models.Model):
    budget = models.IntegerField()
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, db_column='user_id', null=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, db_column='category')
    date_month = models.PositiveIntegerField(default=datetime.now().month)
    date_year = models.PositiveIntegerField(default=datetime.now().year)

    class Meta:
        unique_together = (('category', 'date_month', 'date_year', 'user_id'),)

class Record(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, db_column='user_id')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, db_column='category', null=False)
    amount = models.IntegerField()
    payee = models.CharField(max_length=100, null=True)
    date = models.DateTimeField(default=datetime.now())
    description = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.id}: {self.user_id.username} - {self.amount}"



