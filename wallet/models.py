from django.db import models
from django.contrib import admin
import uuid
from django.contrib.auth.models import User
from django import forms

class Record(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.IntegerField()
    cash = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.uuid}: {self.user.username} - {self.amount}"
        