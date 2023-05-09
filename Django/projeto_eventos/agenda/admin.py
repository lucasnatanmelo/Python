from django.contrib import admin
from agenda.models import Evento, Categoria

# Register your models here.
# Modelos para acesso no painel de admin do django

admin.site.register(Evento)
admin.site.register(Categoria)