import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ifnti_l3.settings')
django.setup()
from notes.models import Eleve,Niveau,Enseignant
import random

# Niveau.objects.all().delete()
# Eleve.objects.all().delete()

# for n in range(1,4):
#     Niveau.objects.create(
#         nom=f"L{n}")
    
# for i in range(10):
#     Eleve.objects.create(

#     )


eleve_data = [
    {

            "matricule":95147895,
            "nom":"Traore",
            "prenom":"Hannatou",
            "sexe":"F",
            "date_naissance":"2003-01-12",
            "niveau_id":7


}
]


for i in eleve_data:
    Eleve.objects.create(**i)


enseignant_data = [
    {

            "matricule":"",
            "nom":"",
            "prenom":"",
            "sexe":"M",
            "date_naissance":"2003-01-12",


}]