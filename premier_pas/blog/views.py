#from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# view avec HttpResponse 

def home(request):
    return HttpResponse("""
        <p>Bienvenue dans l'acceuil </p>
    """)

#passage par identifiant 
def view_article(request, id_article):
	return HttpResponse(
		"Vous avez demandé l'article {0}".format(id_article)
	)
