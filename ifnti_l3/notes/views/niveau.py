from django.shortcuts import render, get_object_or_404
from notes.models import Niveau

def niveau(request, id):
    n = get_object_or_404(Niveau, pk=id)
    return render(request, "notes/niveau.html", {"niveau": n})
