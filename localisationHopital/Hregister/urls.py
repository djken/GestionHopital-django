from django.urls import path
from . import views

urlpatterns = [
    # http://127.0.0.1:8000/
    # Pour la page d'Accueil
    path('', views.home, name='home'),
    
    # Pour Afficher tous les enregistrements
    path('afficher_hopitaux/', views.afficher_hopitaux, name='les-hopitaux'),
    
    # Pour Ajouter un enregistrement utilisant une forme
    path('ajouter_hopital/', views.ajouter_hopital, name= 'ajout-hopital'),
    
    # Pour Modifier un enregistrement utilisant une forme
    path('modifier_hopital/<int:hopital_id>/', views.modifier_hopital, name='modifier-hopital'),
    
    # Pour Afficher un seul et unique enregistrement sans une page
    path('afficher_un_hopital/<int:hopital_id>/', views.afficher_un_hopital, name='un-hopital'),
    
    # pour supprimer un enregistrement
    path('supprimer_un_hopital/<int:hopital_id>/', views.supprimer_un_hopital, name='supprimer-hopital'),
]

# DRY
# 1) URL (Passing the ID)
# 2) View (Fetching ID, then delete the Record)
