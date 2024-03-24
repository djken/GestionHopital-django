from django.shortcuts import render
from django.http import HttpResponse
from .models import TblHospitaltracker 

# Create your views here.
def home(request):
    return render(request, 'hospital/home.html')

def afficher(request):
    hospitals = TblHospitaltracker.objects.all()
    
    return render(request, 'hospital/liste.html', {'hospitals': hospitals})

