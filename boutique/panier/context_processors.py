from .panier import Panier

#Permet de voir le contenu du panier sur toutes les pages
def panier(request):
    return {'panier': Panier(request)}
