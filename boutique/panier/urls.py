from django.urls import path
from . import views

urlpatterns = [
    path('', views.panier_summary, name='panier_summary'),
    path('add/', views.panier_add, name='panier_add'),
    path('delete/', views.panier_delete, name='panier_delete'),
    path('update/', views.panier_update, name='panier_update'),
]