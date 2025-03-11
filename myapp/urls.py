from django.urls import path
from .views import LivroListView
from .views import LivroDetalhesView
from . import views

urlpatterns = [
    path('', LivroListView.as_view(), name='livro-list'), 
    path('detalhes/<int:pk>/', LivroDetalhesView.as_view(), name='livro_detalhe'),
    path('cadastro/', views.LivroCreateView.as_view(), name='livro_cadastro')
]  