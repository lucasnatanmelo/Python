
# Definindo classes
class Evento:
    # self -> Referencia o próprio objeto
    def altera_nome_evento(self, novo_nome):
        print("Alternado nome do evento")
        self.nome = novo_nome


ev = Evento()
ev.nome = "Aula de Python"
print(ev.nome)

ev.altera_nome_evento("Aula de JavaScript")
# Automaticamente passa no argumento o próprio objeto
# ev.altera_nome_evento(ev, "Aula de JavaScript")
print(ev.nome)

# -------------------------------------------------------------
# Construtores


class Novo_Evento:

    # Método construtor padrão
    def __init__(self, nome):
        self.nome = nome
        self.local = "Brasil"

    def altera_nome_evento(self, novo_nome):
        print("Alternado nome do evento")
        self.nome = novo_nome


ev1 = Novo_Evento("Aula de JS")
print(ev1.nome)
print(ev1.local)

# -------------------------------------------------------------
# Método de classes e métodos estáticos


class Pro_Evento:
    # Referencia a instancia do objeto
    def metodo_intancial(self):
        return ("método de instância chamado", self)

    # Referencia a classe geral
    @classmethod
    def metodo_classe(cls):
        return ("método de classe chamado", cls)

    # Método estático padrão conhecido
    @staticmethod
    def metodo_estatico():
        return "estático chamado"


pro_evento = Pro_Evento()

print(pro_evento.metodo_intancial())
print(pro_evento.metodo_classe())
print(pro_evento.metodo_estatico())

print(Pro_Evento.metodo_estatico())

# -------------------------------------------------------------
# Atributo de classe e f-string
# Herança


class Events:

    # Atributo compartilhado entre as classes Events
    id = 1

    # Método construtor padrão
    def __init__(self, nome, local=""):
        self.nome = nome
        self.local = local

        # Soma o atributo dos objetos
        self.id = Events.id
        Events.id += 1

    def imprime_informacoes(self):
        print(f"ID do evento: {self.id}")
        print(f"Nome do evento: {self.nome}")
        print(f"Local do evento: {self.local}")
        print("-----------------------------")

    @classmethod
    def cria_evento_online(cls, nome):
        # Instancia um objeto events pelo cls
        evento = cls(nome, local=f"www.google.com/{cls.id}")
        return evento

    @staticmethod
    def calcula_limite_pessoas_area(area):
        return area*10


class EventoOnline(Events):
    # Sobrescreve o método construtor da classe mãe
    def __init__(self, nome, local):
        # Retoma o id da classe Events
        local = f"www.google.com/id={EventoOnline.id}"

        # super() inicializa pelo método da classe mãe
        super().__init__(nome, local)

    # Sobrescreve o método imprime_informacoes da classe mãe
    def imprime_informacoes(self):
        print(f"ID do evento: {self.id}")
        print(f"Nome do evento: {self.nome}")
        print(f"Link para acessar o evento: {self.local}")
        print("-----------------------------")
