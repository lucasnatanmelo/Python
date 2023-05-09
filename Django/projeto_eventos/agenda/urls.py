from django.urls import path
from agenda.views import exibir_evento, listar_eventos

# URLs relacionadas a agenda
urlpatterns = [
    path("", listar_eventos),
    path("evento", exibir_evento)
]