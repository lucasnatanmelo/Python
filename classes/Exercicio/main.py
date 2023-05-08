from usuario import Usuario
from administrador import Administrador

u = Usuario("Gabriel", "gabriel@exemplo.com")
a = Usuario("Admin", "admin@exemplo.com")
u.imprime_usuario()
# => "Gabriel (gabriel@exemplo.com)
a.imprime_usuario()
# => "Admin (admin@exemplo.com) – Administrador"

c = Administrador("Lucas", "lucas@gmail.com")
c.imprime_usuario()

print(Usuario.quantidade)
# => 3
