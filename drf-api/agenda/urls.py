from django.urls import path
from agenda.views import AgendamentoList, AgendamentoDetail, PrestadorList, get_horarios
# from agenda.views import agendamentos_list, agendamento_detail

urlpatterns = [
    path('agendamentos/', AgendamentoList.as_view()),
    path('agendamentos/<int:id>/', AgendamentoDetail.as_view()),
    path('prestadores/', PrestadorList.as_view()),
    path('horarios/', get_horarios)
]

# urlpatterns = [
#     path('agendamentos/', agendamentos_list),
#     path('agendamentos/<int:pk>/', agendamento_detail)
# ]
