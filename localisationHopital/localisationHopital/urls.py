from django.contrib import admin
from django.urls import path, include
from Hregister import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Hregister.urls')),
    path('gestionutilisateurs/', include('django.contrib.auth.urls')),
    path('gestionutilisateurs/', include('gestionutilisateurs.urls')),
]
