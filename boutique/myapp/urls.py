from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('boutique/', views.product_list, name='boutique'),
    path('produit/<int:pk>/', views.produit, name='produit'),

    # Gestion des produits
    path('supprimer_produit/<int:produit_id>/', views.supprimer_produit, name='supprimer_produit'),
    path('gestion_produit/', views.gestion_produit, name='gestion_produit'),

    #Users

    path('login/', views.login_user, name='login'),
    path('register/', views.register_user, name='register'),
    path('logout/', views.logout_user, name='logout'),

    # Edit du profile (Profile = nom, prenom | Info = adresse, tel, etc. | Password = mot de passe)
    path('profile/', views.profile, name='profile'),
    path('info/', views.info, name='info'),
    path('password/', views.password, name='password'),
    
    

]