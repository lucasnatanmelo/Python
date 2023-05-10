from datetime import date
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.template import loader
from agenda.models import Evento
from django.urls import reverse

# Create your views here.

def listar_eventos(request):

    # Busca os eventos no banco - ORM
    eventos = Evento.objects.all()
    # eventos = Evento.objects.filter(data__gte=date.today()).order_by('-data')

    # Exibir um template listando os eventos
    return render(
        request=request,
        context={"eventos": eventos},
        template_name="agenda/listar_eventos.html"
    )

def exibir_evento(request, id):
    
    # Busca o evento no banco pelo id - ORM
    evento = get_object_or_404(Evento, id=id)

    return render(
        request=request,
        context={"evento": evento},
        template_name="agenda/exibir_evento.html"
    )
# Obs: Incluir em vamomarcar -> settings.py -> INSTALLED_APPS: 'agenda.apps.AgendaConfig'

def participar_evento(request):
    evento_id = request.POST.get("evento_id")   
    evento = get_object_or_404(Evento, id=evento_id)
    evento.participantes += 1
    evento.save()

    return HttpResponseRedirect(reverse('exibir_evento', args=(evento_id,)))