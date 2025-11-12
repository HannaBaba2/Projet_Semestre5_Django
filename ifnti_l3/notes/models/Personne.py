from django.db import models
from django.contrib.auth.models import User

class Personne(models.Model):
    sexe_choix =[

        ('F','Féminin'),
        ('M','Masculin'),
    ]
 
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nom =models.CharField(max_length=50)
    prenom=models.CharField(max_length=50)
    sexe = models.CharField(max_length=1,choices=sexe_choix)
    date_naissance = models.DateField(null=True,blank=True)



    class Meta:
        abstract =True