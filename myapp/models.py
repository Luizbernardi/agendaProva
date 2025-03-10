from django.db import models

class Livro(models.Model):
    titulo = models.CharField(max_length=200, verbose_name="Título")
    autor = models.CharField(max_length=100)
    descricao = models.TextField(verbose_name="Descrição", blank=True, null=True)
    data_publicacao = models.DateField(verbose_name="Data de Publicação")

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = "Livro"
        verbose_name_plural = "Livros"
        ordering = ["-data_publicacao"]