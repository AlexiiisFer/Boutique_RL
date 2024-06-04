from django.urls import path
from . import views

urlpatterns = [

    # Ajouter, supprimer et mettre à jour le panier

    path('', views.panier_summary,name='panier_summary'),
    path('add/', views.panier_add, name='panier_add'),
    path('delete/', views.panier_delete, name='panier_delete'),
    path('update/', views.panier_update, name='panier_update'),

    # Paiement

    path('checkout/', views.checkout, name='checkout'),
    path('paiement/', views.paiement, name='paiement'),

    # Commande

    path('generer_commande/', views.generer_commande, name='generer_commande'),
    path('mes_commandes/', views.commandes_utilisateur, name='commandes_utilisateur'),
    path('admin_commandes/', views.commandes_admin, name='commandes_admin'),
    path('commande/expediee/<int:commande_id>/', views.marquer_commande_expediee, name='marquer_commande_expediee'),
    path('commande_expedier/', views.commandes_expedier, name='commande_expedier'),
    path('commande/<int:pk>/', views.commande_detail, name='commande_detail'),
]