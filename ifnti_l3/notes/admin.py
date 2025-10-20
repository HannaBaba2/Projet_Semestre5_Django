from django.contrib import admin
from .models import Eleve, Enseignant, Niveau, Matiere, Note
from .forms.EleveForm import EleveForm

class EleveAdmin(admin.ModelAdmin):
    form = EleveForm

admin.site.register(Eleve, EleveAdmin)
admin.site.register(Enseignant)
admin.site.register(Niveau)
admin.site.register(Matiere)
admin.site.register(Note)
