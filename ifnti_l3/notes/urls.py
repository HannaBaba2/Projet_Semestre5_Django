app_name = "notes"
from django.urls import path
from .views import index, eleve, matiere, niveau

urlpatterns = [
    path('', index.index, name="index"),
    path('eleves/', eleve.eleves, name="eleves"),
    path('eleve/<int:id>/', eleve.eleve, name="eleve"),
    path('matieres/', matiere.matieres, name="matieres"),
    path('matiere/<int:id>/', matiere.matiere, name="matiere"),
    path('niveau/<int:id>/', niveau.niveau, name="niveau"),
]
