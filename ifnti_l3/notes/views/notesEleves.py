from django.http import FileResponse
from Templating_ifnti.controleur import generate_pdf
from notes.models import Note, Matiere,Eleve
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

def notesEleves(request, matiere_id):
    matiere = Matiere.objects.get(pk=matiere_id)
    notes = Note.objects.filter(matiere=matiere)

    context = {
        "matiere": escape_latex(matiere.nom),
        "notes": [
            {
                "matricule": escape_latex(n.eleve.matricule),
                "nom": escape_latex(n.eleve.nom),
                "prenom": escape_latex(n.eleve.prenom),
                "valeur": n.valeur
            }
            for n in notes
        ]
    }

    pdf_path = generate_pdf(context, template_name="notes_eleves.tex")
    return FileResponse(open(pdf_path, "rb"), content_type="application/pdf")
