from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import Contato , Categoria
from django.views import View

class HomeView(View):
    template_name = 'myapp/home.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
    
class ContatoListView(ListView):
    model = Contato
    template_name = 'myapp/listagem_contatos.html'
    context_object_name = 'contatos'
    paginate_by = 15

class CategoriaListView(ListView):
    model = Categoria
    template_name = 'myapp/listagem_categorias.html'
    context_object_name = 'categorias'
    paginate_by = 15    

class ContatoDetalhesView(DetailView):
    model = Contato
    template_name = 'myapp/contato_detalhe.html'
    context_object_name = 'contato'

class CategoriaDetalhesView(DetailView):
    model = Categoria
    template_name = 'myapp/categoria_detalhe.html'
    context_object_name = 'categoria'

class ContatoCreateView(CreateView):
    model = Contato
    template_name = 'myapp/contato_cadastro.html'
    fields = ['nome', 'telefone', 'email', 'endereco', 'categoria']
    success_url = reverse_lazy('listagem_contatos')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categorias'] = Categoria.objects.all() 
        return context

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        return response
    

class CategoriaCreateView(CreateView):
    model = Categoria
    template_name = 'myapp/categoria_cadastro.html'
    fields = ['nome']
    success_url = reverse_lazy('listagem_categorias')

    
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        return response
    
    
