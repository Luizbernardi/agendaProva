from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=200, verbose_name="Nome")

    def __str__(self):
        return self.nome

class Contato(models.Model):
    nome = models.CharField(max_length=200, verbose_name="Nome")
    telefone = models.CharField(max_length=15, verbose_name="Telefone")
    email = models.EmailField(verbose_name="Email", blank=True, null=True)
    endereco = models.CharField(max_length=255, verbose_name="Endereço")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Contato"
        verbose_name_plural = "Contatos"
        ordering = ["nome"]


