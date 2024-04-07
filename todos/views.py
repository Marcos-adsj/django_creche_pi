from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy
from .models import Todo

class TodoListView(ListView):
    model = Todo

class TodoCreateView(CreateView):
    model = Todo
    fields = ["nome_aluno", "nome_mae", "cpf_mae", "nome_pai", "cpf_pai", "endereco", "telefone", "dt_inicio", "mensalidade", "dt_saida"]
    success_url = reverse_lazy ("todo_list")

class TodoUpdateView(UpdateView):
    model = Todo
    fields = ["nome_aluno", "nome_mae", "cpf_mae", "nome_pai", "cpf_pai", "endereco", "telefone", "dt_inicio", "mensalidade", "dt_saida"]
    success_url = reverse_lazy ("todo_list")