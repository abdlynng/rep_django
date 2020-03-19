from django.urls import path
from . import views

urlpatterns = [
	path('acceuil', views.home),
	path('article/<int:annee>/<int:mois>', views.view_article),
]
