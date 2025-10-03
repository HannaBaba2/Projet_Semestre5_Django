from django.db import models
from .Enseignant import Enseignant


class Matiere(models.Model):
    nom = models.CharField(max_length=50 ,unique=True)
    enseignant = models.ForeignKey(Enseignant, on_delete=models.CASCADE, related_name="matieres")
    niveau= models.ManyToManyField("Niveau",related_name="matieres")

    class Meta:
        verbose_name = "Matière"
        verbose_name_plural = "Matières"


    def __str__(self):
        return self.nom
    
