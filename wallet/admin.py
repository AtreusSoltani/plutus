from django.contrib import admin
from rest_framework.authtoken.admin import TokenAdmin
from wallet.models import Record, Category, Budget

TokenAdmin.raw_id_fields = ['user']
admin.site.register(Record)
admin.site.register(Category)
admin.site.register(Budget)