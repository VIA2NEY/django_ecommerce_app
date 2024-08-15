from django.shortcuts import render, redirect
from .models import CartItem
from django.http import JsonResponse

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


# def checkout_view(request):
#     if request.method == 'POST':
#         # Process payment logic here (e.g., integrating with a payment gateway)
#         CartItem.objects.all().delete()  # Clear the cart after payment
#         return render(request, 'payment_success.html')
#     return redirect('cart_view')
def checkout_view(request):
    if request.method == 'POST':
        CartItem.objects.all().delete()
        
        # Simuler un traitement de paiement
        paiement_reussi = True  # Remplacer par votre logique de traitement
        
        if paiement_reussi:
            # 2. Retourner une réponse JSON indiquant le succès du paiement
            return JsonResponse({'status': 'success', 'message': 'Achat effectué avec succès'})
        else:
            return JsonResponse({'status': 'failure', 'message': 'Erreur lors du paiement'})
    return JsonResponse({'status': 'failure', 'message': 'Requête invalide'}, status=400)