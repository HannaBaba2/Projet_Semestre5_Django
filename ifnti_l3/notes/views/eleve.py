from django.shortcuts import render, get_object_or_404
from notes.models import Eleve

def eleves(request):
    liste = Eleve.objects.all()
    return render(request, "notes/eleves.html", {"eleves": liste})

def eleve(request, id):
    e = get_object_or_404(Eleve, pk=id)
    return render(request, "notes/eleve.html", {"eleve": e})
