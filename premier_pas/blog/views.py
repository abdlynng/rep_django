#from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.shortcuts import redirect

# Create your views here.

# view avec HttpResponse 

def home(request):
    return HttpResponse("""
        <p>Bienvenue dans l'acceuil </p>
    """)

#passage par année et mois
def view_article(request, annee, mois):
		if (annee <= 2020) & (annee >= 0) & (mois <= 12) & (mois >=1):
			return redirect("https://www.djangoproject.com")
		else:
			raise Http404
