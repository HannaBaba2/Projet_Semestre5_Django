from notes.models import Matiere,Note,Eleve,Enseignant,Niveau
from django.shortcuts import render,get_object_or_404
from django.db.models import Avg, Count


# 1 

def nombre(request):
    nb_eleves = Eleve.objects.count()
    nb_matieres = Matiere.objects.count()
    nb_enseignants = Enseignant.objects.count()
    nb_niveaux = Niveau.objects.count()

def moyenn_eleves(request):

    moyenne_eleves=Note.objects.all().order_by(Eleve)
    return moyenne_eleves

def moyenne_matiere(request):

    moyenne_matiere=Note.objects.all().order_by(Matiere)
    return moyenne_matiere


def first_eleves5(request):
    first_5=Eleve.objects.first([5])


def statistique(request,id):

    
    liste1 = Niveau.objects.filter(niveau_id="id")

        
   

    return render(request, "notes/statistique.html", {"statistique": liste1})

def statistiques(request):

    liste1 = Matiere.objects.all()
    liste2 = Eleve.objects.all()
    liste3= Enseignant.objects.all()
    liste4 = Note.objects.all()
        
   

    return render(request, "notes/statistiques.html", {"statistiques": liste1})





