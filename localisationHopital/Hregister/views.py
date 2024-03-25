from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Hopitaltracker 
from django.views.decorators.csrf import csrf_protect
from .forms import HopitalForm

# Create your views here.
def home(request):
    return render(request, 'hopitaux/home.html')

def afficher_hopitaux(request):
    hopitaux = Hopitaltracker.objects.all()
    
    return render(request, 'hopitaux/tous_les_hopitaux.html', {'hopitaux': hopitaux})

@csrf_protect
def ajouter_hopital(request):
    submitted = False

    if request.method == "POST":
        form = HopitalForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/ajouter_hopital?submitted=True')
    else:
        form = HopitalForm()
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'hopitaux/ajouter_un_hopital.html', {'form':form, 'submitted':submitted})

def modifier_hopital(request, hopital_id):
    hopital = Hopitaltracker.objects.get(pk=hopital_id)
    
    # return HttpResponse(hopital)
    form = HopitalForm(request.POST or None, instance=hopital)
    if form.is_valid():
        form.save()
        return redirect('les-hopitaux')
   
    return render(request, 'hopitaux/modifier_un_hopital.html', {'hopital':hopital, 'form':form})


# 
def afficher_un_hopital(request, hopital_id):
    hopital = Hopitaltracker.objects.get(pk=hopital_id)
    
    return render(request, 'hopitaux/afficher_un_hopital.html', {'hopital': hopital})
