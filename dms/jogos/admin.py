from django.contrib import admin

# Register your models here.
from jogos.models import Jogadores,Competicao

# Register your models here.
@admin.register(Competicao)
class Jogos_Admin(admin.ModelAdmin):
    def queryset(self, request):
       qs = super(MyModelAdmin, self).queryset(request)
    def __unicode__(self):
        return self.nome
    list_editable=('status',)
    list_display = ("nome", "local","data","hora","status", )
    
@admin.register(Jogadores)
class Jogos_Admin(admin.ModelAdmin):
    def queryset(self, request):
       qs = super(MyModelAdmin, self).queryset(request)
    def __unicode__(self):
        return self.nome
    list_editable=('tempo','competicao')
    list_display = ("nome", "competicao","tempo", )
  
    