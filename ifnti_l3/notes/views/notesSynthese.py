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




def notesSynthese(request):
    eleves_data = []

    for elv in Eleve.objects.all():
        notes = Note.objects.filter(eleve=elv)
        synthese = {}
        for n in notes:
            mat = escape_latex(n.matiere.nom)
            synthese.setdefault(mat, []).append(n.valeur)

        synthese_list = [
            {"matiere": mat, "moyenne": round(sum(v)/len(v), 2)}
            for mat, v in synthese.items()
        ]

        eleves_data.append({
            "nom": escape_latex(elv.nom),
            "prenom": escape_latex(elv.prenom),
            "matricule": escape_latex(elv.matricule),
            "synthese": synthese_list
        })

    context = {"eleves": eleves_data}
    pdf_path = generate_pdf(context, template_name="notes_synthese.tex")
    return FileResponse(open(pdf_path, "rb"), content_type="application/pdf")
