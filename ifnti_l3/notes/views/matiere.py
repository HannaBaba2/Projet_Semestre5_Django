from django.shortcuts import render, get_object_or_404
from notes.models import Matiere

def matieres(request):
    liste = Matiere.objects.all()
    return render(request, "notes/matieres.html", {"matieres": liste})

def matiere(request, id):
    m = get_object_or_404(Matiere, pk=id)
    return render(request, "notes/matiere.html", {"matiere": m})
