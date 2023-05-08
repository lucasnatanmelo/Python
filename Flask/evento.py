import json


class Evento:

    # Atributo compartilhado entre as classes Evento
    id = 1

    # Método construtor padrão
    def __init__(self, nome, local=""):
        self.nome = nome
        self.local = local

        # Soma o atributo dos objetos
        self.id = Evento.id
        Evento.id += 1

    def imprime_informacoes(self):
        print(f"ID do evento: {self.id}")
        print(f"Nome do evento: {self.nome}")
        print(f"Local do evento: {self.local}")
        print("-----------------------------")

    def to_json(self):
        return json.dumps({
            "id": self.id,
            "local": self.local,
            "nome": self.nome
        })

    @classmethod
    def cria_evento_online(cls, nome):
        # Instancia um objeto events pelo cls
        evento = cls(nome, local=f"www.google.com/{cls.id}")
        return evento

    @staticmethod
    def calcula_limite_pessoas_area(area):
        return area*10