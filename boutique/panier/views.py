from django.shortcuts import render, redirect, get_object_or_404
from .panier import Panier
from myapp.models import Produit
from django.http import JsonResponse

# Create your views here.

def panier_summary(request):
    panier = Panier(request)
    panier_produits = panier.get_prods()
    context = {
        'panier_produits': panier_produits
    }
    return render(request, 'panier_summary.html', context)

def panier_add(request):
    # Récupération du panier
    panier = Panier(request)
    # Test si la requête est de type POST
    if request.POST.get('action') == 'post':
        # Récupération des données du formulaire
        produit_id = int(request.POST.get('produit_id'))
        # Récupération du produit
        produit = get_object_or_404(Produit, id=produit_id)
        # Ajout du produit au panier
        panier.add(produit=produit)
        # Obtient le nombre de produits dans le panier
        panier_quantite = panier.__len__()
        # Retourne le nombre de produits dans le panier
        Response = JsonResponse({'qtite': panier_quantite})
          
        return Response


def panier_delete(request):
    return render(request, 'panier_delete.html')

def panier_update(request):
    return render(request, 'panier_update.html')

