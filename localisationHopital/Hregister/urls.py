from django.urls import path
from . import views

urlpatterns = [
    # http://127.0.0.1:8000/
    path('', views.home), # Example: www.hopitaux-haiti.ht
    path('afficher_hopitaux/', views.afficher_hopitaux, name='les_hopitaux')
]

# DRY
# URL, View(Vue = Fonction Python), Template (HTML)

# Database
# Model