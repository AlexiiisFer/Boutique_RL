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

    def add(self, produit, quantite):
        produit_id = str(produit.id)
        produit_qty = str(quantite)
        if produit_id in self.panier:
            pass
        else:
            self.panier[produit_id] = {'prix' : str(produit.price)}
            self.panier[produit_id] = int(produit_qty)

        self.session.modified = True
    
    def __len__(self):
        return len(self.panier)

    def get_prods(self):
        produit_ids = self.panier.keys()
        produits = Produit.objects.filter(id__in=produit_ids)
        return produits
    
    def get_quants(self):
        quantite = self.panier
        return quantite
    
    def update(self, produit, quantite):
        produit_id = str(produit)
        produit_qty = int(quantite) 
        # Le panier
        lepanier = self.panier
        #Mise à jour de la quantité
        lepanier[produit_id] = produit_qty
        self.session.modified = True
        return lepanier

    def delete(self, produit):
        {'4':3, '2':1}
        produit_id = str(produit)
        if produit_id in self.panier:
            del self.panier[produit_id]
        self.session.modified = True

    def panier_total(self):
        produit_ids = self.panier.keys()
        produits = Produit.objects.filter(id__in=produit_ids)
        quantite = self.panier
        total = 0
        
        for key, value in quantite.items():
            key = int(key)
            for produit in produits:
                if produit.id == key:
                    if produit.is_promo:
                        total += produit.promo_price * value
                    else:
                        total += produit.price * value
        return total
    


    
    
    
    
    