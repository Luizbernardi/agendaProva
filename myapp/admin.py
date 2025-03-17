from django.contrib import admin
from .models import Contato, Categoria


@admin.register(Contato)
class ContatoAdmin(admin.ModelAdmin):
    list_display = ("nome", "telefone", "email", "endereco")
    search_fields = ("nome", "telefone", "email")
    list_filter = ("nome",)

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ("nome",)
    search_fields = ("nome",)
    list_filter = ("nome",)