from django.urls import path
from .views import ContatoListView, ContatoDetalhesView, ContatoCreateView, HomeView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('listagem/', ContatoListView.as_view(), name='listagem_contatos'),
    path('detalhes/<int:pk>/', ContatoDetalhesView.as_view(), name='contato_detalhe'),
    path('cadastro/', ContatoCreateView.as_view(), name='contato_cadastro')
]
