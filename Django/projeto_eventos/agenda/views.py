from django.http.response import HttpResponse
from django.shortcuts import render
from django.template import loader

from agenda.models import eventos

# Create your views here.


def index(request):
    return HttpResponse("Olá mundo!")


def exibir_evento(request):
    # evento = eventos[0]
    evento = {
        "nome": "Teste",
        "categoria": "categoria A",
        "local": "Manaus"
    }
    # template = loader.get_template("agenda/exibir_evento.html")
    # rendered_template = template.render(
    #       context={"evento": evento},
    #       request=request
    #     )
    # return HttpResponse(rendered_template)

    return render(
        request=request,
        context={"evento": evento},
        template_name="agenda/exibir_evento.html"
    )
# Obs: Incluir em vamomarcar -> settings.py -> INSTALLED_APPS: 'agenda.apps.AgendaConfig'
