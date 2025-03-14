from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import Contato
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

class ContatoDetalhesView(DetailView):
    model = Contato
    template_name = 'myapp/contato_detalhe.html'
    context_object_name = 'contato'

class ContatoCreateView(CreateView):
    model = Contato
    template_name = 'myapp/contato_cadastro.html'
    fields = ['nome', 'telefone', 'email', 'endereco']
    success_url = reverse_lazy('listagem_contatos')

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        return response
    
    
