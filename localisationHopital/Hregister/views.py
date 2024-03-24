from django.shortcuts import render
from django.http import HttpResponse
from .models import Hopitaltracker 

# Create your views here.
def home(request):
    return render(request, 'hospitaux/home.html')

def afficher_hopitaux(request):
    hopitaux = Hopitaltracker.objects.all()
    
    return render(request, 'hospitaux/tous_les_hopitaux.html', {'hopitaux': hopitaux})