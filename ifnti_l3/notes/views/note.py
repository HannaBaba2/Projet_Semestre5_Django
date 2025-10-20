
from django.shortcuts import render, get_object_or_404,redirect
from notes.models import Eleve, Matiere, Note
from notes.forms.NoteForm import NoteForm

def add_note(request, eleve_id, matiere_id):
    eleve = get_object_or_404(Eleve, pk=eleve_id)
    matiere = get_object_or_404(Matiere, pk=matiere_id)

    if matiere not in eleve.matieres.all():
        raise Exception(f"L'élève {eleve.nom} ne suit pas la matière {matiere.nom}")

    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.eleve = eleve
            note.matiere = matiere
            note.save()
            return redirect(f'/notes/eleve/{eleve.matricule}/')
    else:
        form = NoteForm()

    return render(request, "notes/add_note.html", {"form": form, "eleve": eleve, "matiere": matiere})



    
def add_notes(request, matiere_id):
    matiere = get_object_or_404(Matiere, pk=matiere_id)
    eleves = Eleve.objects.filter(niveau__in=matiere.niveau.all())

    if request.method == 'POST':
        print(request.POST)  
        for e in eleves:

            valeur = request.POST.get(f'note_{e.matricule}')
            print(f"Élève {e.matricule}: valeur={valeur}")  

            if valeur and valeur.strip():
                try:
                    Note.objects.update_or_create(
                        eleve=e,
                        matiere=matiere,
                        defaults={'valeur': float(valeur)}
                    )
                except Exception as err:
                    print(f"⚠️ Erreur en créant la note de {e.nom}: {err}")
        return redirect('notes:matieres')

    return render(request, "notes/add_notes.html", {
        "matiere": matiere,
        "eleves": eleves
    })
