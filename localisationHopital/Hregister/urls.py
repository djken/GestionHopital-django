from django.urls import path
from . import views

urlpatterns = [
    # http://127.0.0.1:8000/
    path('', views.home),
    path('liste/', views.afficher)
]

# DRY