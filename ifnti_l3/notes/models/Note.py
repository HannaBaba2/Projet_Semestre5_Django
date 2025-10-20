from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from .Eleve import Eleve
from .Matiere import Matiere

class Note(models.Model):
    valeur = models.FloatField(validators=
                               [MinValueValidator(0),
                                MaxValueValidator(20)],null=True, blank=True)
    eleve = models.ForeignKey(Eleve, on_delete=models.CASCADE,related_name="notes")
    matiere = models.ForeignKey(Matiere, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.eleve} - {self.matiere} : {self.valeur}"



    