
#Creer une fichier urls.py dans les app <produit>
from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_commande),
    path('ajout_commande', views.ajouter_commande,name='ajout_commande'),
    path('ajout_commande/<str:pk>', views.modifier_commande, name='modifier_commande'),
    path('supprimer_commande/<str:pk>', views.supprimer_commande, name='supprimer_commande')
]