from django.urls import path
from . import views

urlpatterns = [
    # http://127.0.0.1:8000/
    path('', views.home, name='home'),
    path('afficher_hopitaux/', views.afficher_hopitaux, name='les-hopitaux'),
    path('ajouter_hopital/', views.ajouter_hopital, name= 'ajout-hopital'),
    path('modifier_hopital/<int:hopital_id>/', views.modifier_hopital, name='modifier-hopital'),
    path('afficher_un_hopital/<int:hopital_id>/', views.afficher_un_hopital, name='un-hopital'),
]

# DRY