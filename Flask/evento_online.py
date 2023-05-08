from evento import Evento


class EventoOnline(Evento):
    # Sobrescreve o método construtor da classe mãe
    def __init__(self, nome, _=""):
        # Retoma o id da classe Evento
        local = f"www.google.com/id={EventoOnline.id}"

        # super() inicializa pelo método da classe mãe
        super().__init__(nome, local)

    # Sobrescreve o método imprime_informacoes da classe mãe
    def imprime_informacoes(self):
        print(f"ID do evento: {self.id}")
        print(f"Nome do evento: {self.nome}")
        print(f"Link para acessar o evento: {self.local}")
        print("-----------------------------")
