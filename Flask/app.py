from flask import Flask, jsonify, abort, make_response, request, json
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

"""
Importante:

obj.dumps() dict => json
obj.loads() json => dict

"""
# Descrição: Retorna todos os eventos cadastrados 
# Método: GET
@app.route("/api/eventos/")
def lista_eventos(): #view
    eventos_dict = []
    for ev in eventos:
        # __dict__ transforma as propriedades para o tipo dict
        eventos_dict.append(ev.__dict__)
    return jsonify(eventos_dict)

# Descrição: Cria e armazena um evento
# Método: POST
@app.route("/api/eventos/", methods=["POST"])
def criar_evento():
    # Parsing
    data = json.loads(request.data)
    nome = data.get("nome")
    local = data.get("local")

    # Validação
    if not nome:
        abort(400, "'nome' previsa ser informado!")

    # Criando evento
    if local:
      novo_evento = Evento(nome=nome, local=local)
    else:
      novo_evento = EventoOnline(nome=nome)

    eventos.append(novo_evento)

    # Retorna ao usuário a rota para acessar o novo evento criado
    return {
        "id": novo_evento.id,
        "url": f"/api/eventos/{novo_evento.id}"
    }

# Descrição: Retorna um evento pelo id
# Método: GET
@app.route("/api/eventos/<int:id>/")
def detalhar_evento(id): #view
    
    # Caso encontre, irá retornar 
    ev = get_evento_or_404(id)
    
    # Caso não, Relaciona com o errorhandler
    abort(404, "Evento não encontrado")

# Descrição: Deleta um evento pelo id
# Método: DELETE
@app.route("/api/eventos/<int:id>/", methods=["DELETE"])
def deletar_evento(id): #view
    # Caso encontre, irá retornar e deletar
    ev = get_evento_or_404(id)
    eventos.remove(ev)
    return jsonify(id=id)

# Descrição: Edita um evento pelo id por completo
# Método: PUT
@app.route("/api/eventos/<int:id>/", methods=["PUT"])
def editar_evento(id): #view
    # Parsing
    data = request.get_json()
    nome = data.get("nome")
    local = data.get("local")

    # Validação
    if not nome:
        abort(400, "'nome' previsa ser informado!")
    if not local:
        abort(400, "'local' previsa ser informado!")

    ev = get_evento_or_404(id)
    ev.nome = nome
    ev.local = local

    return jsonify(ev.__dict__)

# Descrição: Edita um evento pelo id parcialmente
# Método: PATCH
@app.route("/api/eventos/<int:id>/", methods=["PATCH"])
def editar_evento_parcial(id): #view
    # Parsing
    data = request.get_json()

    ev = get_evento_or_404(id)
    if "nome" in data.keys():
        nome = data.get("nome")
        if not nome:
            abort(400, "'nome' precisa ser informado")
        ev.nome = nome

    if "local" in data.keys():
        local = data.get("local")
        if not local:
            abort(400, "'local' precisa ser informado")
        ev.local = local

    return jsonify(ev.__dict__)


# ------------------------- Erros Handlers -------------------------
# Error type: 400
@app.errorhandler(400)
def nao_encontrado(erro):
    data = {"erro" : str(erro)}
    return (jsonify(data), 400)

    # Mesma coisa
    # return (jsonify(erro=str(erro)), 404)

# Error type: 404
@app.errorhandler(404)
def nao_encontrado(erro):
    data = {"erro" : str(erro)}
    return (jsonify(data), 404)

    # Mesma coisa
    # return (jsonify(erro=str(erro)), 404)

# ------------------------- Utils -------------------------

def get_evento_or_404(id):
    for ev in eventos:
        if ev.id == id:
            return ev
    abort(404, "Evento não encontrado")