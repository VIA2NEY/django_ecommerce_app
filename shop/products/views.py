from django.shortcuts import render, get_object_or_404

from .models import Product

# Create your views here.
def home_index(request):
    products = Product.objects.all()
    return render(request, 'home_index.html', {'products': products})

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    related_products = Product.objects.exclude(id=product_id)[:4]  # Limitez à 4 produits
    return render(
        request, 
        'product_detail.html', 
        {
            'product': product,
            'related_products': related_products
        }
    )

def cart(request):
    # Logic to handle cart items
    return render(request, 'cart.html')