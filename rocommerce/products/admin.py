from django.contrib import admin

# Register your models here.

from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'image_url', 'description','type', 'brand', 'price', 'available')  
    search_fields = ('name', 'type', 'brand')  

admin.site.register(Product, ProductAdmin)