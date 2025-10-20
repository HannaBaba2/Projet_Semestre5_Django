from django.shortcuts import render, redirect,get_object_or_404
from notes.models import Eleve
from notes.forms.EleveForm import EleveForm


def eleves(request):
    liste = Eleve.objects.all()
    return render(request, "notes/eleves.html", {"eleves": liste})

def eleve(request, id):
    e = get_object_or_404(Eleve, pk=id)
    return render(request, "notes/eleve.html", {"eleve": e})



def add_eleve(request):
    if request.method == "POST":
        form = EleveForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("notes:eleves")
    else:
        form = EleveForm()
    return render(request, "notes/add_eleve.html", {"form": form})


def update_eleve(request, id):
    from notes.models import Eleve

    eleve = get_object_or_404(Eleve, pk=id)
    if request.method == "POST":
        form = EleveForm(request.POST, instance=eleve)
        if form.is_valid():
            form.save()
            return redirect("notes:eleves")
    else:
        form = EleveForm(instance=eleve)
    return render(request, "notes/update_eleve.html", {"form": form, "eleve": eleve})

