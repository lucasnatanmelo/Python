from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from agenda.models import Agendamentos
from agenda.serializers import AgendamentoSerializer

# Create your views here.

def agendamento_detail(request, id):
    obj = get_object_or_404(Agendamentos, id=id)
    serializer = AgendamentoSerializer(obj)

    return JsonResponse(serializer.data)
