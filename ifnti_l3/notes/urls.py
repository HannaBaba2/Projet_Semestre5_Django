app_name = "notes"
from django.urls import path
from .views import index, statistique,eleve, matiere, niveau,stats_views,note,enseignant

urlpatterns = [
    path('', index.index, name="index"),
    path('eleves/', eleve.eleves, name="eleves"),
    path("eleve/add/", eleve.add_eleve, name="add_eleve"),
    path('eleve/<str:id>/', eleve.eleve, name="eleve"),
    path("enseignant/add/", enseignant.add_enseignant, name="add_enseignant"),
    # path('statistiques/', statistique.statistiques, name="statistiques"),
   
    path("eleve/update/<str:id>/", eleve.update_eleve, name="update_eleve"),
    path("enseignant/update/<int:id>/", enseignant.update_enseignant, name="update_enseignant"),
    path('statistiques/', stats_views.statistiques, name="stats"),
    path("note/add/<str:eleve_id>/<int:matiere_id>/", note.add_note, name="add_note"),
    path("notes/add_notes/<int:matiere_id>/", note.add_notes, name="add_notes"),
    path('statistiques/<int:id>/', statistique.statistique, name="statistique"),
    path('matieres/', matiere.matieres, name="matieres"),
    path('matiere/<int:id>/', matiere.matiere, name="matiere"),
    path('niveau/<int:id>/', niveau.niveau, name="niveau"),
]
