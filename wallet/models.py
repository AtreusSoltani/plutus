from django.db import models
from django.contrib import admin
import uuid

class IAMUser(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4)
    username = models.CharField(max_length=100, unique=True)
    
    def __str__(self):
        return self.username
admin.site.register(IAMUser)

class Record(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.ForeignKey(IAMUser, on_delete=models.CASCADE)
    amount = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.uuid}: {self.user.username} - {self.amount}"
admin.site.register(Record)