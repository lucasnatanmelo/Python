from datetime import date
from django.test import TestCase, Client

from agenda.models import Categoria, Evento

# Create your tests here.

class TestPaginaInicial(TestCase):
    def test_list_eventos(self):
        client = Client()
        response = client.get("/")

        # Verifica se a reposta irá conter o elemento html
        # self.assertContains(response, "<th>Nome</th>")

        # Verifica se o template irá carregar corretamente
        self.assertTemplateUsed(response, "agenda/listar_eventos.html")

class TestListagemDeEventos(TestCase):
    def test_evento_com_data_de_hoje_e_exibido(self):
        categoria = Categoria()
        categoria.name = "Backend"
        categoria.save()

        evento = Evento()
        evento.nome = "Aula de Python"
        evento.categoria = categoria
        evento.local = "Rio de Janeiro"
        evento.data = date.today()
        evento.save()

        client = Client()
        response = client.get("/")
        self.assertContains(response, "Aula de Python")
        self.assertEqual(list(response.context["eventos"][0]), evento)