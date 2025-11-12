from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render, redirect
from notes.forms.EnseignantForm import EnseignantForm
@login_required
@permission_required('notes.add_enseignant', raise_exception=True)


def add_enseignant(request):
    if request.method == "POST":
        form = EnseignantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("notes:matieres")
    else:
        form = EnseignantForm()
    return render(request, "notes/add_enseignant.html", {"form": form})

@login_required
@permission_required('notes.update_enseignant', raise_exception=True)

def update_enseignant(request, id):
    from django.shortcuts import get_object_or_404
    from notes.models import Enseignant

    enseignant = get_object_or_404(Enseignant, pk=id)
    if request.method == "POST":
        form = EnseignantForm(request.POST, instance=enseignant)
        if form.is_valid():
            form.save()
            return redirect("notes:matieres")
    else:
        form = EnseignantForm(instance=enseignant)
    return render(request, "notes/update_enseignant.html", {"form": form, "enseignant": enseignant})
