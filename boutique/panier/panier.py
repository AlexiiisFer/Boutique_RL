from myapp.models import Produit

class Panier():
    def __init__(self, request):
        self.session = request.session

        # On récupère le panier de l'utilisateur s'il existe, sinon on crée un panier vide
        panier = self.session.get('session_key')
                                  
        if 'session_key' not in self.session:
            panier = self.session['session_key'] = {}

        #Panier sur tout le site
        self.panier = panier

    def add(self, produit):
        produit_id = str(produit.id)
        if produit_id in self.panier:
            pass
        else:
            self.panier[produit_id] = {'prix' : str(produit.price)}

        self.session.modified = True
    
    def __len__(self):
        return len(self.panier)

    def get_prods(self):
        produit_ids = self.panier.keys()
        produits = Produit.objects.filter(id__in=produit_ids)
        return produits