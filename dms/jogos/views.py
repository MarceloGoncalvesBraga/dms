from django.views.generic import TemplateView, ListView
from django.shortcuts import render, HttpResponse,redirect
from django.urls import reverse_lazy ,path

from jogos.models import Jogadores,Competicao
from jogos.forms import Jogos_Form,Competicao_Form

# Create your views here.

class Index_Template(ListView):
    template_name = 'jogos/home.html'
    def get(self, request, *args, **kwargs):
   
       model = Jogadores,Competicao
       tipo = request.session.get('tipo')
       print(tipo)
       return render(request,self.template_name ,{
        'competicoes' : Competicao.objects.filter(status= 1),
        'competicoes_encerrada' : Competicao.objects.filter(status= 0),
        'listar_todos':Jogadores.objects.all(),
        'listar_encerrados': Jogadores.objects.order_by("-competicao")[:12],
        #'banner_footer':   Website_Banner.objects.filter(local="footer"),
    
       })

class Competicoes_Views(ListView):
    
    template_name = 'jogos/competicao.html'
    def get(self, request, *args,slug, **kwargs):
   
       model = Jogadores,Competicao
       tipo = Competicao.objects.filter(slug=slug)
       if Competicao.objects.filter(slug=slug).exists():
           for i in tipo:
              inscrito = i.id
         
         #tipo = request.session.get('tipo')
           return render(request,self.template_name ,{
        'competicoes' : Competicao.objects.filter(slug=slug),
        'ranquim' : Jogadores.objects.filter(competicao=inscrito),
        'listar_todos': Jogadores.objects.filter(competicao=inscrito),
        'listar_encerrados': Jogadores.objects.order_by("-competicao")[:12],
        #'banner_footer':   Website_Banner.objects.filter(local="footer"),
    
           })
       return redirect("jogos:home")
     
class Jogo_Add_Jogador(ListView):
    
    template_name = 'jogos/add_competidor.html'
    model= Jogadores
    
    def get(self, request, *args, **kwargs):   
        
        form = Jogos_Form()
        return render(request,self.template_name ,{
        'form' :form,
        })
        
    def post(self, request, *args, **kwargs):
     if request.method == "POST":
            
        form = Jogos_Form(request.POST)
        if form.is_valid():
            model= Jogadores
            id = request.POST["competicao"]
            print(id)
            if Competicao.objects.filter(id= id).filter(status = 0):
                   return render(request,self.template_name ,{
                  'form' :form,
                  'msg': "Competicao encerrada"
                   })
            else:
             form.save()
             return render(request,self.template_name ,{
             'form' :form,
             'msg': "Competidor salvo"
             })
        else:
            return render(request,self.template_name ,{
            'form' :form,
            'msg': "Erro ao salvar"
            })
            
        return redirect("jogos:add_jogos")

class Jogo_Add_Competicao(ListView):
    
    template_name = 'jogos/add_competicao.html'
    model= Competicao
    
    def get(self, request, *args, **kwargs):   
        
        form = Competicao_Form
        return render(request,self.template_name ,{
        'form' :form,
        'competicoes' : Competicao.objects.all(),
        'competicoes_encerrada' : Competicao.objects.filter(status= 0),
        })
        
    def post(self, request, *args, **kwargs):
     if request.method == "POST":
            
        form = Competicao_Form(request.POST)
        if form.is_valid():
            model= Competicao
            
            form.save()
            return render(request,self.template_name ,{
             'form' :form,
             'msg': "Competicao salva salvo",
            'competicoes' : Competicao.objects.all(),
            'competicoes_encerrada' : Competicao.objects.filter(status= 0),
             })
        else:
            return render(request,self.template_name ,{
            'form' :form,
            'msg': "Erro ao salvar",
            'competicoes' : Competicao.objects.all(),
            'competicoes_encerrada' : Competicao.objects.filter(status= 0),
            })
            
     return redirect("jogos:add_competicao")

class Jogos_Alterar(ListView):
    template_name = 'jogos/usuario/usuario.html'
    model = Jogadores,Competicao
    
    def get(self, request, *args, **kwargs):
      
        if request.session.get('user_id'):
            
          model = Jogadores,Competicao
          id = request.session.get('id')
          
          if Jogadores.objects.filter(id = id).exists():
            jogo = Jogadores.objects.get(id=id)
            jogoform=Jogadores(instance=jogo)
                        
            return render(request,self.template_name ,{
                'jogoform':jogoform,     
       
            })
          else:
           return redirect("jogos:home")
        else:
         return redirect("jogos:home")
    
    def post(self, request, *args, **kwargs):
        if request.method == "POST":
           jogo = Jogadores.objects.get(id=id)
           
           form = Jogos_Form(request.POST,request.FILES,instance=jogo)
           
           if form.is_valid():
                form.save()
                  # instance = form
                user = request.session.get('home')
                return redirect('jogos:home')