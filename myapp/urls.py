from django.urls import path
from .views import ContatoListView, ContatoDetalhesView, ContatoCreateView, HomeView, CategoriaListView, CategoriaDetalhesView, CategoriaCreateView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('contato/listagem', ContatoListView.as_view(), name='listagem_contatos'),
    path('contato/detalhes/<int:pk>/', ContatoDetalhesView.as_view(), name='contato_detalhe'),
    path('contato/cadastro/', ContatoCreateView.as_view(), name='contato_cadastro'),
    path('categoria/listagem', CategoriaListView.as_view(), name='listagem_categorias'),
    path('categoria/detalhes/<int:pk>/', CategoriaDetalhesView.as_view(), name='categoria_detalhe'),
    path('categoria/cadastro/', CategoriaCreateView.as_view(), name='categoria_cadastro'),

]
