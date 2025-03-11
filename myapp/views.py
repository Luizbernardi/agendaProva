from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import Livro

class LivroListView(ListView):
    model = Livro
    template_name = 'myapp/listagem_livros.html'
    context_object_name = 'livros'
    paginate_by = 5

class LivroDetalhesView(DetailView):
    model = Livro
    template_name = 'myapp/livro_detalhe.html'
    context_object_name = 'livro'

class LivroCreateView(CreateView):
    model = Livro
    template_name = 'myapp/livro_cadastro.html'
    fields = ['titulo', 'autor', 'descricao', 'data_publicacao']
    success_url = reverse_lazy('livro-list')

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        # Adicione aqui qualquer lógica adicional que você precise após o POST
        return response
