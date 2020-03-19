#from django.shortcuts import render
from django.http import HttpResponse, Http404

# Create your views here.

# view avec HttpResponse 

def home(request):
    return HttpResponse("""
        <p>Bienvenue dans l'acceuil </p>
    """)

#passage par année et mois
def view_article(request, annee, mois):
		if (annee <= 2020) & (annee >= 0) & (mois <= 12) & (mois >=1):
			return HttpResponse(
				"Article du {0}/{1}".format(mois, annee)
			)
		else:
			raise Http404
