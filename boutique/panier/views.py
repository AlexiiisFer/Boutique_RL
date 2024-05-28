from django.shortcuts import render, redirect, get_object_or_404
from .panier import Panier
from myapp.models import Produit
from django.http import JsonResponse
from django.contrib import messages

# Create your views here.

def panier_summary(request):
    panier = Panier(request)
    panier_produits = panier.get_prods()
    quantite = panier.get_quants()
    
    context = {
        
        'panier_produits': panier_produits,
        'quantite': quantite,
    }
    return render(request, 'panier_summary.html', context)

def panier_add(request):
    # Récupération du panier
    panier = Panier(request)
    # Test si la requête est de type POST
    if request.POST.get('action') == 'post':
        # Récupération des données du formulaire
        produit_id = int(request.POST.get('produit_id'))
        # Récupération de la quantité des produits
        produit_qty = int(request.POST.get('produit_qty'))
        # Récupération du produit
        produit = get_object_or_404(Produit, id=produit_id)
        # Ajout du produit au panier
        panier.add(produit=produit, quantite=produit_qty)
        # Obtient le nombre de produits dans le panier
        panier_quantite = panier.__len__()
        # Retourne le nombre de produits dans le panier
        Response = JsonResponse({'qtite': panier_quantite})
          
        return Response


def panier_delete(request):
    panier = Panier(request)
    if request.POST.get('action') == 'post':
		# Get stuff
        produit_id = int(request.POST.get('produit_id'))
		# Call delete Function in Cart
        panier.delete(produit=produit_id)

        response = JsonResponse({'produit':produit_id})
		#return redirect('cart_summary')
        messages.success(request, ("Article supprimé du panier..."))
        return response

def panier_update(request):
    panier = Panier(request)
    if request.POST.get('action') == 'post':
		# Get stuff
        produit_id = int(request.POST.get('produit_id'))
        produit_qty = int(request.POST.get('produit_qty'))

        panier.update(produit=produit_id, quantite=produit_qty)

        response = JsonResponse({'qty':produit_qty})
		#return redirect('cart_summary')
        messages.success(request, ("Le panier a été mis à jour..."))
        return response

