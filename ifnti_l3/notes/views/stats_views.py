from django.http import HttpResponse
from django.shortcuts import render
from django.db.models import Avg
from notes.models import(
    Niveau,
    Matiere,
    Eleve,
    Note,
    Enseignant
    )

def statistiques(request):

    nb_eleves=Eleve.objects.count()
    nb_enseignant=Enseignant.objects.count()
    nb_matiere=Matiere.objects.count()
    nb_note=Note.objects.count()


    # moyenne_general_par_eleve=[]

    eleves=Eleve.objects.all()


    for e in eleves:

        # notes=Note.objects.filter(eleve=e).values_list("valeur",flat=True)

        # somme=sum(notes)
        # print(somme)
        #moyenne_eleve=e.note_set.all()
        #moyenne_eleve=e.notes.all()

        # moyennes_eleves=Note.objects.aggregate(moyenne_generale=Avg("valeur"))
        moyenne_general_par_eleve=Eleve.objects.annotate(moyenne_generale=Avg("notes"))

        # moyennes_eleves["eleves"]=e
        # moyenne_general_par_eleve.append(moyennes_eleves)



    data={

        "nb_eleves":nb_eleves,
        "nb_enseignant":nb_enseignant,
        "nb_matiere":nb_matiere,
        "nb_note":nb_note,

    }

    print(data)
    return HttpResponse("Stats")