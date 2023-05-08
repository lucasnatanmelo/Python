class Usuario:

    # Atributo compartilhado entre as classes Usuario
    quantidade = 0

    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

        # Auto incrementa o número de instâncias entre as classes
        self.quantidade = Usuario.quantidade
        Usuario.quantidade += 1

    def imprime_usuario(self):
        print(f"{self.nome} ({self.email})")
