from django.contrib import admin
from .models import Eleve, Enseignant, Niveau, Matiere, Note
from .forms.EleveForm import EleveForm


@admin.register(Eleve)
class EleveAdmin(admin.ModelAdmin):

    form = EleveForm

    list_display = ('matricule', 'nom', 'prenom', 'sexe', 'niveau', 'date_naissance')
    list_display_links = ('matricule', 'nom')        
    list_editable = ('niveau',)                     
    search_fields = ('matricule', 'nom', 'prenom')   
    list_filter = ('niveau', 'sexe')                
    date_hierarchy = 'date_naissance'               
    readonly_fields = ('matricule',)                 
    filter_horizontal = ('matieres',)                
    list_per_page = 20                              
    show_full_result_count = False
    save_on_top = True                              
    empty_value_display = '- Aucune donnée -'

    fieldsets = (
        ('Informations personnelles', {
            'fields': (('nom', 'prenom'), 'sexe', 'date_naissance')
        }),
        ('Informations académiques', {
            'fields': ('niveau', 'matieres', 'matricule'),
            'description': "Sélectionnez le niveau de l'élève et les matières suivies."
        }),
    )


@admin.register(Enseignant)
class EnseignantAdmin(admin.ModelAdmin):
    list_display = ('nom', 'prenom', 'date_naissance')
    search_fields = ('nom', 'prenom')


@admin.register(Niveau)
class NiveauAdmin(admin.ModelAdmin):
    list_display = ('nom',)
    search_fields = ('nom',)


@admin.register(Matiere)
class MatiereAdmin(admin.ModelAdmin):
    list_display = ('nom', 'enseignant')
    search_fields = ('nom',)
    list_filter = ('enseignant',)


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ('eleve', 'matiere', 'valeur')
    list_filter = ('matiere', 'eleve')
    search_fields = ('eleve__nom', 'eleve__prenom', 'matiere__nom')
    list_editable = ('valeur',)
    save_on_top = True


admin.site.site_header = "IFNTI - Administration"
admin.site.site_title = "IFNTI - Gestion académique"
admin.site.index_title = "Tableau de bord administratif"
