from django.http import FileResponse, Http404
from notes.models import Eleve,Matiere,Niveau,Note
from Templating_ifnti.controleur import generate_pdf
import os

import re

def escape_latex(text):
    if text is None:
        return ""

    text = str(text)

    replacements = {
        '\\': r'\textbackslash{}',
        '{': r'\{',
        '}': r'\}',
        '$': r'\$',
        '&': r'\&',
        '%': r'\%',
        '#': r'\#',
        '_': r'\_',
        '^': r'\^{}',
        '~': r'\~{}',
    }

    pattern = re.compile("|".join(re.escape(k) for k in replacements))
    return pattern.sub(lambda m: replacements[m.group(0)], text)

# 🔹 Vue pour tous les élèves
def listEleves(request):
    eleves_qs = Eleve.objects.all().values(
        "matricule", "nom", "prenom", "sexe", "date_naissance"
    )

    eleves = [
        {k: escape_latex(v) for k, v in e.items()}
        for e in eleves_qs
    ]

    context = {"eleves": eleves}

    try:
        pdf_path = generate_pdf(context)
    except Exception as e:
        raise Http404(f"Erreur PDF : {e}")

    if not os.path.exists(pdf_path):
        raise Http404("PDF introuvable")

    return FileResponse(open(pdf_path, "rb"), content_type="application/pdf")

def liste_niveauElv(request, niveau_id):
    eleves_qs = Eleve.objects.filter(niveau_id=niveau_id).values(
        "matricule", "nom", "prenom", "sexe", "date_naissance"
    )
    eleves = [{k: escape_latex(v) for k, v in e.items()} for e in eleves_qs]
    context = {"eleves": eleves}

    try:
        pdf_path = generate_pdf(context)
    except Exception as e:
        raise Http404(f"Erreur PDF : {e}")

    if not os.path.exists(pdf_path):
        raise Http404("PDF introuvable")

    return FileResponse(open(pdf_path, "rb"), content_type="application/pdf")


