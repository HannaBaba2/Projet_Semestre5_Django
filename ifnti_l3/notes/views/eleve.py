from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render, redirect,get_object_or_404
from notes.models import Eleve
from notes.forms.EleveForm import EleveForm


# @login_required
# @permission_required('notes.eleves', raise_exception=True)

def eleves(request):
    liste = Eleve.objects.all()
    return render(request, "notes/eleves.html", {"eleves": liste})


# @login_required
# @permission_required('notes.eleve', raise_exception=True)

def eleve(request, id):
    e = get_object_or_404(Eleve, pk=id)
    return render(request, "notes/eleve.html", {"eleve": e})


@login_required
@permission_required('notes.add_eleve', raise_exception=True)
def add_eleve(request):
    if request.method == "POST":
        form = EleveForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("notes:eleves")
    else:
        form = EleveForm()
    return render(request, "notes/add_eleve.html", {"form": form})


@login_required
@permission_required('notes.update_eleve', raise_exception=True)

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

