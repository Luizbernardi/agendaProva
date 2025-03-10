from django.contrib import admin
from .models import Livro  

@admin.register(Livro)
class LivroAdmin(admin.ModelAdmin):
    list_display = ("titulo", "autor", "data_publicacao")
    search_fields = ("titulo", "autor")
    list_filter = ("data_publicacao",)