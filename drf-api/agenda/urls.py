from django.urls import path
from agenda.views import agendamento_detail

urlpatterns = [
    # path('agendamentos/', agendamentos_list),
    path('agendamentos/<int:id>/', agendamento_detail)
]
