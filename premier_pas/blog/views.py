#from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# view avec HttpResponse 

def home(request):
    return HttpResponse("""
        <p>Bienvenue dans l'acceuil </p>
    """)
