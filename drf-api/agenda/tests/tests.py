from datetime import datetime, timezone
import json
from rest_framework import APITestCase

from agenda.models import Agendamento

# Create your tests here.

"""
Python(dict) para JSON/
json.dumps({}) => '{}'

JSON para python(dict)
json.loads(b'{}') => {}
"""

class TestListagemAgendamentos(APITestCase):
  def test_listagem_vazia(self):
    response = self.client.get("api/agendamentos/")
    data = json.loads(response.content)
    self.assertEqual(data, [])

  def test_listagem_de_agendamentos_criados(self):
    ...
    # Implements test here
    # tzinfo = timezone.utc -> set time zone as utc - ISO 8601
    Agendamento.objects.create(
      data_horario = datetime(2023, 5, 15, tzinfo=timezone.utc),
      nome_cliente = "Alice",
      email_cliente = "alice@gmail.com",
      telefone_cliente = "999999999"
    )

    agendamento_esperado_serializado = {
      "id" : 1,
      "data_horario" : "2022-03-15T00:00:00Z",
      "nome_cliente": "Alice",
      "email_cliente" : "alice@gmail.com",
      "telefone_cliente" : "99999999"
    }

    response = self.client.get("api/agendamentos/")
    data = json.loads(response.content)
    self.assertDictEqual(data[0], agendamento_esperado_serializado)


class TestCriacaoAgendamento(APITestCase):
  def test_cria_agendamento(self):

    agendamento_esperado_serializado = {
      "data_horario" : "2022-03-15T00:00:00Z",
      "nome_cliente": "Alice",
      "email_cliente" : "alice@gmail.com",
      "telefone_cliente" : "99999999"
    }

    response = self.client.post("api/agendamentos/", data = agendamento_esperado_serializado, format="json")
    response_get = self.client.get("/api/agendamentos/")
    agendamento_criado = Agendamento.objects.get()

    self.assertEqual(agendamento_criado.data_horario, datetime(2022, 3, 15, tzinfo=timezone.utc))
    self.assertEqual(response.status_code, 201)

  def test_quando_request_e_invalido_retorna_400(self):
    ...

from unittest import mock  
class TestGetHorarios(APITestCase):
  @mock.patch("agenda.libs.brasil_api.is_feriado", return_value=True)
  def test_quando_data_e_feriado_retorna_lista_vazia(self, _):
    response = self.client.get("/api/horarios/?data=2022-12-25")
    self.assertEqual(response.data, [])

  @mock.patch("agenda.libs.brasil_api.is_feriado", return_value=False)
  def test_quando_data_e_dia_comum_retorna_lista_com_horarios(self, _):
    response = self.client.get("api/horarios/?data=2022-12-20")
    self.assertNotEqual(response.data, [])
    self.assertEqual(response.data[0], datetime(2022, 10, 3, 9, tzinfo = timezone.utc))
    self.assertEqual(response.data[-1], datetime(2022, 10, 17, 30, tzinfo = timezone.utc))