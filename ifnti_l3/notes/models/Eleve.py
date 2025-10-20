from django.db import models
from .Personne import Personne
from .Niveau import Niveau
from .Matiere import Matiere


class Eleve(Personne):
    
    matricule = models.CharField(max_length=20, primary_key=True)
    niveau=models.ForeignKey(Niveau,on_delete=models.CASCADE)
    # matieres = models.ManyToManyField("Matiere", related_name="eleves")
    matieres = models.ManyToManyField(
        "Matiere",
        related_name="eleves",
        blank=True,
        verbose_name="Laissez vide pour associer automatiquement les matières du niveau"
    )




    class Meta:
        verbose_name = "Élève"
        verbose_name_plural = "Élèves"

    def __str__(self):
        return f"{self.prenom} {self.nom} {self.sexe} {self.date_naissance}"
    

