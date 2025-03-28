from django.urls import path
from .views import ContatoCreateView, HomeView, CategoriaCreateView
from . import views

urlpatterns = [
    path('', HomeView.index, name='home'),
    path('contato/listagem', views.contato_list_view, name='listagem_contatos'),
    path('contato/detalhes/<int:pk>/',views.contato_detalhes_view, name='contato_detalhe'),
    path('contato/cadastro/', ContatoCreateView.as_view(), name='contato_cadastro'),
    path('categoria/listagem', views.categoria_list_view, name='listagem_categorias'),
    path('categoria/detalhes/<int:pk>/', views.categoria_detalhes_view, name='categoria_detalhe'),
    path('categoria/cadastro/', CategoriaCreateView.as_view(), name='categoria_cadastro'),

]


