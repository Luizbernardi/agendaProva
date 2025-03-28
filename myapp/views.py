from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import Contato , Categoria
from django.views import View
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


class HomeView(View):
    def index(request):
        if request.user.is_authenticated:  
            contatos = Contato.objects.all()  
            return render(request, 'myapp/listagem_contatos.html', {'contatos': contatos})
        else:
            contatos = Contato.objects.all()  
            return render(request, 'myapp/home.html', {'contatos': contatos})
    

@login_required(login_url='login')
def contato_list_view(request):
    contatos = Contato.objects.all()
    return render(request, 'myapp/listagem_contatos.html', {'contatos': contatos})

@login_required(login_url='login')
def categoria_list_view(request):
            categorias = Categoria.objects.all()
            return render(request, 'myapp/listagem_categorias.html', {'categorias': categorias})

@login_required(login_url='login')
def contato_detalhes_view(request, pk):
    contato = Contato.objects.get(pk=pk)
    return render(request, 'myapp/contato_detalhe.html', {'contato': contato})

@login_required(login_url='login')
def categoria_detalhes_view(request, pk):
    categoria = Categoria.objects.get(pk=pk)
    return render(request, 'myapp/categoria_detalhe.html', {'categoria': categoria})


class ContatoCreateView(LoginRequiredMixin, CreateView):
    model = Contato
    template_name = 'myapp/contato_cadastro.html'
    fields = ['nome', 'telefone', 'email', 'endereco', 'categoria']
    success_url = reverse_lazy('listagem_contatos')
    login_url = 'login' 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categorias'] = Categoria.objects.all()
        return context

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        return response
    
class CategoriaCreateView(LoginRequiredMixin, CreateView):
    model = Categoria
    template_name = 'myapp/categoria_cadastro.html'
    fields = ['nome']
    success_url = reverse_lazy('listagem_categorias')
    login_url = 'login' 

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        return response
    
    

