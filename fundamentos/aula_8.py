valor = 21

if (valor < 10):
    print("Maior que 10")
elif (valor <= 20 and valor >= 10):
    print("Entre 20 e 10")
else:
    print("Deu errado")


# truthy and falsy

# falsy -> 0, "", None

# truthy -> whatelse

new_value = 0

if (new_value):
    print("new_value is truthy")
else:
    print("new_value is falsy")
