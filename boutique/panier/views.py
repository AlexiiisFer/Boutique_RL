from django.utils import timezone
from django.shortcuts import render, redirect, get_object_or_404
from .panier import Panier
from myapp.models import Produit
from django.http import JsonResponse
from django.contrib import messages
from myapp.models import AdresseFacturation, AdresseLivraison, Produit
from myapp.forms import UserInfoForm, AdresseLivraisonForm
from .forms import PaiementForm, UserUnlogForm
from .models import Commande, CommandeArticle
from django.contrib.auth.models import User

# Fonctionnalité du Panier

def panier_summary(request):
    panier = Panier(request)
    panier_produits = panier.get_prods()
    quantite = panier.get_quants()
    panier_total = panier.panier_total()

    quantite_options = {}
    for produit in panier_produits:
        stock_disponible = produit.stock
        quantite_options[produit.id] = range(1, stock_disponible + 1)

    context = {
        'total': panier_total,
        'panier_produits': panier_produits,
        'quantite': quantite,
        'quantite_options': quantite_options,
        
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
        messages.success(request, ("Article ajouté au panier..."))
          
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
        messages.success(request, ("Le panier a été mis à jour..."))
        return response
    
# Fonctionnalité du paiement, vérification de la commande


def checkout(request):
    panier = Panier(request)
    quantite = panier.get_quants()
    panier_produits = panier.get_prods()
    panier_total = panier.panier_total()

    # Si l'utilisateur est connecté, il peut accéder à la page de paiement
    if request.user.is_authenticated:
        livraison_user = AdresseLivraison.objects.get(user__id=request.user.id)
        livraison_form = AdresseLivraisonForm(request.POST or None, instance=livraison_user)
        return render(request, 'checkout.html', {'quantite': quantite,'total': panier_total,'panier_produits': panier_produits, 'livraison_form': livraison_form})
    # Sinon, l'utilisateur doit se connecter pour accéder à la page de paiement
    else:
        userunlog = UserUnlogForm()
        livraison_form = AdresseLivraisonForm(request.POST or None)
        return render(request, 'checkout.html',{'quantite': quantite,'total': panier_total,'panier_produits': panier_produits,'livraison_form': livraison_form, 'userunlog': userunlog})
    

def paiement(request):
    if request.POST:
        panier = Panier(request)
        quantite = panier.get_quants()
        panier_produits = panier.get_prods()
        panier_total = panier.panier_total()
        paiement_form = PaiementForm()

        # Créer une variable pour garder les infos pour les commandes
        ma_livraison = request.POST
        request.session['ma_livraison'] = ma_livraison

        context = {
            'quantite': quantite,
            'total': panier_total,
            'panier_produits': panier_produits,
            'paiement_form': paiement_form,
            'livraison_info': request.POST,
        }

        if request.user.is_authenticated:
            return render(request, 'paiement.html', context)
        else:
            pass

        return render(request, 'paiement.html', context)
    # Sinon, l'utilisateur doit se connecter pour accéder à la page de paiement
    else:
        messages.error(request, "Formulaire invalide")
        return redirect('login')
    
def generer_commande(request):
    if request.POST:
        panier = Panier(request)
        panier_produits = panier.get_prods()
        quantite = panier.get_quants()
        paiement_form = PaiementForm(request.POST)
        ma_livraison = request.session.get('ma_livraison')
        prix_total = panier.panier_total()

        adresse_livraison = f"{ma_livraison['livraison_titre']}\n{ma_livraison['livraison_rue']}\n{ma_livraison['livraison_ville']}\n{ma_livraison['livraison_code_postal']}\n{ma_livraison['livraison_pays']}"

        if request.user.is_authenticated:
            if paiement_form.is_valid():
                # Commande total
                user = request.user
                name = user.first_name + " " + user.last_name
                email = user.email
                creer_commande = Commande(user=user,name=name, email=email, address=adresse_livraison, prix_total=prix_total)
                creer_commande.save()

                # Envoyer les infos de la commande pour Commande Article

                commande_id = creer_commande.pk
                for produit in panier_produits:
                    produit_id = produit.id
                    if produit.is_promo:
                        prix = produit.promo_price
                    else:
                        prix = produit.price
                    
                    for key, value in quantite.items():
                        if int(key) == produit.id:
                            creer_commande_produit = CommandeArticle(commande_id=commande_id,user=user, produit_id=produit_id, prix=prix, quantitee=value)
                            creer_commande_produit.save()

                for key in list(request.session.keys()):
                    if key == "session_key":
                        del request.session[key]

                messages.success(request, "Votre commande a été passée avec succès")
                return redirect('home')
        else:

            if paiement_form.is_valid():  
                name = ma_livraison['name']
                email = ma_livraison['email']
                creer_commande = Commande(name = name, email=email, address=adresse_livraison, prix_total=prix_total)
                creer_commande.save()

                 # Envoyer les infos de la commande pour Commande Article

                commande_id = creer_commande.pk
                for produit in panier_produits:
                    produit_id = produit.id
                    if produit.is_promo:
                        prix = produit.promo_price
                    else:
                        prix = produit.price
                    
                    for key, value in quantite.items():
                        if int(key) == produit.id:
                            creer_commande_produit = CommandeArticle(commande_id=commande_id, produit_id=produit_id, prix=prix, quantitee=value)
                            creer_commande_produit.save()
                
                for key in list(request.session.keys()):
                    if key == "session_key":
                        del request.session[key]

                messages.success(request, "Votre commande a été passée avec succès")
                return redirect('home')
            

    else:
        messages.error(request, "Formulaire invalide")
        return redirect('paiement')
    
def commandes_utilisateur(request):
    if request.user.is_authenticated:
        user = request.user
        commandes = Commande.objects.filter(user=user)
        context = {
            'commandes': commandes
        }
        return render(request, 'mes_commandes.html', context)
    else:
        messages.error(request, "Vous devez être connecté pour accéder à cette page")
        return redirect('login')
    
def commandes_admin(request):
    if request.user.is_authenticated:
        if request.user.is_staff:
            commandes = Commande.objects.all()
            context = {
                'commandes': commandes
            }
            return render(request, 'commandes_admin.html', context)
        else:
            messages.error(request, "Vous n'avez pas les droits pour accéder à cette page")
            return redirect('home')
    else:
        messages.error(request, "Vous devez être connecté pour accéder à cette page")
        return redirect('login')
    
def marquer_commande_expediee(request, commande_id):
    commande = get_object_or_404(Commande, id=commande_id)
    commande.expedie = True
    commande.date_expedie = timezone.now()  # Assurez-vous d'importer timezone
    commande.save()
    messages.success(request, "Commande marquée comme expédiée")
    return redirect('commandes_admin')  # Remplacez par le nom de la vue qui affiche la liste des commandes

def commandes_expedier(request):
    if request.user.is_authenticated:
        if request.user.is_staff:
            commandes = Commande.objects.all()
            context = {
                'commandes': commandes
            }
            return render(request, 'commande_expedier.html', context)
        else:
            messages.error(request, "Vous n'avez pas les droits pour accéder à cette page")
            return redirect('home')
    else:
        messages.error(request, "Vous devez être connecté pour accéder à cette page")
        return redirect('login')
    
def commande_detail(request, pk):
    commande = get_object_or_404(Commande, id=pk)
    
    if request.user.is_authenticated:
        if request.user.is_superuser or request.user == commande.user:
            articles = CommandeArticle.objects.filter(commande=pk)
            context = {
                'commande': commande,
                'articles': articles
            }
            return render(request, 'commande_detail.html', context)
        else:
            messages.error(request, "Vous n'avez pas les droits pour accéder à cette page")
            return redirect('home')
    else:
        messages.error(request, "Vous devez être connecté pour voir cette page")
        return redirect('login')
  