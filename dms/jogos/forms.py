
from django import forms
from jogos.models import Jogadores,Competicao

class Jogos_Form(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(Jogos_Form, self).__init__(*args, **kwargs)
        for name in self.fields.keys():
            self.fields[name].widget.attrs.update({'class': 'form-control edit-jog',}) 
    class Meta:
        model = Jogadores
        fields = ['nome','competicao','tempo','distancia','tentativas']
        labels = {
        'nome':'Nome:',
        'competicao':'Competicao:',
        'tempo':'Tempo:',
        'distancia':'Distancia:',
        'tentativas':'Tentativa:'
 
       } 
class Competicao_Form(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(Competicao_Form, self).__init__(*args, **kwargs)
        for name in self.fields.keys():
            self.fields[name].widget.attrs.update({'class': 'form-control edit-comp ',}) 
    class Meta:
        model = Competicao
        fields = ['nome','local','data','hora','status']
        labels = {
        'nome':'Nome:',
        'local':'Local:',
        'data':'Data:',
        'hora':'Hora:',
        'status':'Status:'
 
       } 