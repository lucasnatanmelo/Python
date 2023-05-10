from django.urls import path
from agenda.views import exibir_evento, listar_eventos, participar_evento

# URLs relacionadas a agenda
urlpatterns = [
    path("eventos", listar_eventos, name="lista_eventos"),
    path("eventos/<int:id>/", exibir_evento, name="exibir_evento"),
    path("participar/", participar_evento, name="participar_evento")
]