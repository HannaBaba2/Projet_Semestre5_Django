from django.db import models
from .Eleve import Eleve
from .Matiere import Matiere

class Note(models.Model):
    valeur = models.FloatField(null=True, blank=True)
    eleve = models.ForeignKey(Eleve, on_delete=models.CASCADE)
    matiere = models.ForeignKey(Matiere, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.eleve} - {self.matiere} : {self.valeur}"
