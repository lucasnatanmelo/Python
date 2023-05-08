from flask import Flask
from evento import Evento
from evento_online import EventoOnline

# __name__ -> nome do arquivo padrão
app = Flask(__name__)

ev_online = EventoOnline("Live de Python")
ev2_online = EventoOnline("Live de JavaScript")
ev = Evento("Aula de Python", "Manaus")
eventos = [ev_online, ev2_online, ev, ev_online]

@app.route("/")
def index():
    return """
      <h1> Flask configurado com sucesso!!!!</h1>
    """

