from django.shortcuts import render, redirect
from .models import CartItem

# Create your views here.

# def cart_view(request):
#     cart_items = CartItem.objects.all()  # You can filter by user if needed
#     total_price = sum(item.get_total_price() for item in cart_items)
#     return render(
#         request, 
#         'index_paiement.html', 
#         {
#             'cart_items': cart_items, 
#             'total_price': total_price
#         }
#     )
def cart_view(request):
    cart_items = CartItem.objects.all()  # Tu peux filtrer par utilisateur si nécessaire
    total_price = sum(item.get_total_price() for item in cart_items)

    context = {
        'cart_items': cart_items,
        'total_price': total_price,
    }

    return render(request, 'index_paiement.html', context)


def checkout_view(request):
    if request.method == 'POST':
        # Process payment logic here (e.g., integrating with a payment gateway)
        CartItem.objects.all().delete()  # Clear the cart after payment
        return render(request, 'payment_success.html')
    return redirect('cart_view')
