from django.db import models

# Create your models here.


class Categoria(models.Model):
    # unique = True -> Impossibilita valores duplicados
    nome = models.CharField(max_length=256, unique=True)

    def __str__(self):
        return f"{self.nome} <self.id>"

class Evento(models.Model):
    nome = models.CharField(max_length=256)

    # ForeignKey -> Chave estrangeira
    #on_delete = modelos.SER_NULL -> ao excluir a categoria, será transformado para null
    categoria = models.ForeignKey(
        Categoria, 
        on_delete=models.SET_NULL, 
        null=True
    )

    #blank=True -> Valor pode ser branco
    local = models.CharField(max_length=256, blank=True)
    link = models.CharField(max_length=256, blank=True)
    data = models.DateField(null=True)