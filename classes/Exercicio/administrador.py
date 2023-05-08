from usuario import Usuario


class Administrador(Usuario):

    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

        # Auto incrementa o número de instâncias entre as classes
        self.quantidade = Usuario.quantidade
        Usuario.quantidade += 1

    def imprime_usuario(self):
        print(f"{self.nome} ({self.email}) - Administrador")
