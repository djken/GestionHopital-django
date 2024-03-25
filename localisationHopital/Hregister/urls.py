from django.urls import path
from . import views

urlpatterns = [
    # http://127.0.0.1:8000/
    path('', views.home), # Example: www.hopitaux-haiti.ht
    path('afficher_hopitaux/', views.afficher_hopitaux, name='les_hopitaux')
]

# ***************************************
# 1) URL, 
# 2) View(Vue = Fonction Python)
# 3) Template (HTML)
#******************************************


# Database
# Model