from django.urls import path
from . import views


urlpatterns = [
    path('', views.home_index, name='home_index'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
    path('cart/', views.cart, name='cart'),
]