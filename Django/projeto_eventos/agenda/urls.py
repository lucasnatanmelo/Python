from django.urls import path
from agenda.views import exibir_evento, index

# URLs relacionadas a agenda
urlpatterns = [
    path("", index),
    path("evento", exibir_evento)
]