from django.db import models

from django.db import models

class Todo(models.Model):
    nome_aluno = models.CharField(max_length=100, null=False, blank=False)
    nome_mae = models.CharField(max_length=100, null=False, blank=False)
    cpf_mae = models.CharField(max_length=100, null=False, blank=False) 
    nome_pai = models.CharField(max_length=100, null=False, blank=False) 
    cpf_pai = models.CharField(max_length=100, null=False, blank=False) 
    endereco = models.CharField(max_length=100, null=False, blank=False) 
    telefone = models.CharField(max_length=100, null=False, blank=False) 
    dt_inicio = models.CharField(max_length=100, null=False, blank=False) 
    mensalidade = models.CharField(max_length=100, null=False, blank=False) 
    created_at = models.DateTimeField(auto_now_add=True, null=False, blank=False)
    dt_saida = models.DateField(null=False, blank=False) 
    finished_at = models.DateField(null=True) 