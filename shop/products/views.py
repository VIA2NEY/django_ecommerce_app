from django.shortcuts import render, get_object_or_404, redirect

from .models import Product
from paiement.models import CartItem

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

def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    quantity = int(request.POST.get('quantity', 1))

    # Vérifier si l'article est déjà dans le panier
    cart_item, created = CartItem.objects.get_or_create(product=product)
    
    # Si l'article est déjà dans le panier, augmenter la quantité
    if not created:
        cart_item.quantity += quantity
    else:
        cart_item.quantity = quantity

    cart_item.save()

    return redirect('cart_view') 


# def cart_view(request):
#     return redirect('cart_view')