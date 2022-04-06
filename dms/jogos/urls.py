
from jogos.views import  Index_Template,Competicoes_Views
from jogos.views import   Jogos_Alterar

from jogos.views import  Jogo_Add_Competicao,Jogo_Add_Jogador

from django.shortcuts import render, HttpResponse,redirect
from django.urls import reverse_lazy ,include,re_path,path
from django.conf.urls.static import static
from django.conf import settings
#from django.conf.urls import url



app_name = 'jogos'


urlpatterns = [
    # GET /
    path('', Index_Template.as_view(), name="home"),
    path('competicao/<slug:slug>', Competicoes_Views.as_view(), name="competicao"),
    path('add/competicao',Jogo_Add_Competicao.as_view(), name='add_competicao'),

    path('add/jogador',Jogo_Add_Jogador.as_view(), name='add_jogador'),

    path('jogos/alterar/',Jogos_Alterar.as_view(), name='alterar_jogos'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
