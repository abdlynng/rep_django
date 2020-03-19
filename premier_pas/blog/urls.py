from django.urls import path
from . import views

urlpatterns = [
	path('acceuil', views.home),
	path('article/<int:id_article>/', views.view_article),
]
