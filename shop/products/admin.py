from django.contrib import admin

from .models import Product

# Register your models here.
# Rendre Product modifiable par l'admin
admin.site.register(Product)