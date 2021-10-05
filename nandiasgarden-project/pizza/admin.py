from django.contrib import admin
from .models import Pizza, Size

@admin.register(Pizza)
class AdminPizza:
    pass

@admin.register(Size)
class AdminSize:
    pass