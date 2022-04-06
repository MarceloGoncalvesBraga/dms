from django.db import models
from datetime import datetime, date
from django.urls import reverse
from autoslug import AutoSlugField

# Create your models here.
class Competicao(models.Model):
     
    STATUS = (
    ('0', 'Encerrado'),
    ('1', 'Em Andamento'), 
    ('2', 'Em Espera'), )  
 
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=135, verbose_name='Nome')
    local = models.CharField(null =False,max_length=255, verbose_name='Local')
    slug = AutoSlugField(max_length=255,unique=True,populate_from='nome',verbose_name='slug',editable=False)

    data = models.CharField(null=True,blank=True,max_length=135, verbose_name='Data')
    hora = models.CharField(null=True,blank=True,max_length=135, verbose_name='Hora da Partida')
    status = models.CharField(default='1', null=True,blank=True,max_length=35,choices=STATUS)
    def __str__(self):
        
            return self.nome
    def get_absolute_url(self):    
           return reverse('jogos:competicao', args=[str(self.slug)])
    def get_rota(self):
            return reverse("jogos:competicao", kwargs={"slug": self.slug})
        
    class Meta:
       db_table = u'tipo'
       verbose_name = 'Competicao'
       verbose_name_plural = 'Competicao'
       
       
class Jogadores(models.Model):
    TENTATIVAS = (
    ('1', '1'),
    ('2', '2'), 
    ('3', '3'), )  
    id = models.AutoField(primary_key=True)
    
    nome = models.CharField(null =False,max_length=255, verbose_name='Nome Completo ')
    
    competicao = models.ForeignKey(Competicao, on_delete=models.CASCADE,related_name='Competicao')
    tempo = models.CharField(null=True,blank=True,max_length=135, verbose_name='Tempo em Segundos, Distancia em Metros')
    distancia = models.CharField(null=True,blank=True,max_length=135, verbose_name='Tempo em Segundos, Distancia em Metros')
    tentativas = models.CharField(default='1', null=True,blank=True,max_length=5,choices=TENTATIVAS,verbose_name='Tentativa ')
   

    created = models.DateField(auto_now=True)
    updated = models.DateField(auto_now=True)
    
    def __str__(self):
        return self.nome
 
    def get_nome(self):
           return self.nome
       
       
    class Meta:
        db_table = u'jogos'
        verbose_name = 'Jogador'
        verbose_name_plural = 'Jogadores'
        ordering = ['tempo']
