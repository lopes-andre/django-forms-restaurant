from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from .models import Pizza, Size

@admin.register(Pizza)
class AdminPizza(ModelAdmin):
    pass

@admin.register(Size)
class AdminSize(ModelAdmin):
    pass