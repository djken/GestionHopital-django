from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Hopitaltracker 
from django.views.decorators.csrf import csrf_protect
from .forms import HopitalForm

# Create your views here.
def home(request):
    return render(request, 'hospitaux/home.html')

def afficher_hopitaux(request):
    hopitaux = Hopitaltracker.objects.all()
    
    return render(request, 'hospitaux/tous_les_hopitaux.html', {'hopitaux': hopitaux})

@csrf_protect
def ajouter_hopital(request):
    submitted = False

    if request.method == "POST": # HTTP Method
        form = HopitalForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/ajouter_hopital?submitted=True')
    else:
        form = HopitalForm()
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'hospitaux/ajouter_un_hopital.html', {'form':form, 'submitted':submitted})