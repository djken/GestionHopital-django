from django.urls import path
from . import views

urlpatterns = [
    # http://127.0.0.1:8000/
    path('', views.home),
    path('afficher_hopitaux/', views.afficher_hopitaux, name='les_hopitaux')
]

# DRY