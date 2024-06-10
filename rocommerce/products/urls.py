from django.urls import path
from .views import get_products, add_products, update_products, delete_products

urlpatterns = [
    path ('getproducts/', get_products, name='getProducts'),
    path('addproducts/', add_products, name='addProducts'),
    path('updateproducts/<int:id>/', update_products, name='updateProducts'),
    path('deleteproducts/<int:id>/', delete_products, name='delete_products'),
]