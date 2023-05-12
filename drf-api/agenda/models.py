from django.db import models

# Create your models here.

class Agendamentos(models.Model):
    data_horario = models.DateTimeField()
    nome_cliente = models.CharField(max_length=256)
    email_cliente = models.EmailField()
    telefone_cliente = models.CharField(max_length=20)