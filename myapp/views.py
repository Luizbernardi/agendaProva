from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views.generic import ListView
from .models import Livro

class LivroListView(ListView):
    model = Livro
    template_name = 'myapp/listagem_livros.html'
    context_object_name = 'livros'
    paginate_by = 5

    