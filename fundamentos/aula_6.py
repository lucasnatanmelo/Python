# Operadores lógicos
# not
# and
# or

idade = 16
maior_de_idade = idade >= 18
menor_de_idade = not maior_de_idade

print("menor_de_idade", menor_de_idade)

# and
usuario_correto = True
senha_correta = True

sucesso = usuario_correto and senha_correta
print("Acesso ao usuário", sucesso)

# or
idade = 14
idade_minima = 16
acompanhado_pelos_pais = False

pode_assistir = idade >= idade_minima or acompanhado_pelos_pais

print("Pode assistir", pode_assistir)
