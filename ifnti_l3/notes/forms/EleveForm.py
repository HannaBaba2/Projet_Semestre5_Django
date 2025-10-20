# notes/forms/EleveForm.py
from django import forms
from notes.models import Eleve

class EleveForm(forms.ModelForm):
    class Meta:
        model = Eleve
        fields = ['nom', 'prenom', 'sexe', 'date_naissance', 'niveau', 'matieres']
        labels = {
            'nom': 'Nom de famille',
            'prenom': 'Prénom',
            'sexe': 'Sexe (M/F)',
            'date_naissance': 'Date de naissance',
            'niveau': 'Niveau',
            'matieres': 'Matières suivies'
        }

    def clean_nom(self):
        nom = self.cleaned_data.get('nom', '')
        if any(ch.isdigit() for ch in nom):
            raise forms.ValidationError("Le nom ne doit pas contenir de chiffres.")
        return nom

    def clean_prenom(self):
        prenom = self.cleaned_data.get('prenom', '')
        if any(ch.isdigit() for ch in prenom):
            raise forms.ValidationError("Le prénom ne doit pas contenir de chiffres.")
        return prenom

    def clean(self):
        cleaned_data = super().clean()
        niveau = cleaned_data.get("niveau")
        matieres = cleaned_data.get("matieres")

        if not niveau or not matieres:
            return cleaned_data

        for m in matieres.all():
            if niveau not in m.niveau.all():
                raise forms.ValidationError(
                    f"La matière « {m.nom} » ne correspond pas au niveau « {niveau.nom} »."
                )

        return cleaned_data

    def save(self, commit=True):
        instance = super().save(commit=False)

        nom = instance.nom[:2].upper()
        prenom = instance.prenom[:2].upper()
        sexe = instance.sexe[0].upper()
        annee = instance.date_naissance.year

        instance.matricule = f"{nom}{prenom}{sexe}{annee}"

        if commit:
            instance.save()
            if not instance.matieres.exists():
                instance.matieres.set(instance.niveau.matieres.all())


        
        return instance
