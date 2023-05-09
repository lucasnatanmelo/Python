n = int(input("Insira um número: "))

is_prime = True
i = 2

while(i <= (n//2)):

    if(n % i == 0):
        is_prime = False

    i += 1


prime_response = 'É primo' if is_prime else 'Não é primo'
print(n , str(prime_response))

notas = [4, 2.2, 5, 1, 3]

print(notas[1])
print(notas[3])

notas.sort(reverse=True)

x = notas.pop()

print(x)

notas.insert(0, 8)

print(notas)

y = notas.pop(2)

print(notas)

# Lista heterogenea

pessoas = [
    ["Lucas", 23],
    ["Gabriel", 22],
    ["Fulano", 11]
]

age_total_sum = 0
age_average = 0

iterator = 0
while(iterator < len(pessoas)):
    age_total_sum += pessoas[iterator][1]
    print("Current", pessoas[iterator])
    iterator += 1

age_average = age_total_sum / len(pessoas)

print("Age Total Sum", age_total_sum)
print("Age Average", age_average)


# Tuples

notas_tuple = ("Lucas", 24, True)

nome, idade, admin = notas_tuple

print(nome, idade, admin)

pessoas_tuple = [
    ("Lucas", 23),
    ("Gabriel", 22),
    ("Fulano", 11)
]

# Set -> Conjuntos

usuarios = {"alice", "bob", "carlos"}
usuarios_2 = set(["alice", "bob", "lucas"])

print(usuarios.union(usuarios_2))
print(usuarios.intersection(usuarios_2))
print(usuarios.difference(usuarios_2))

eh_igual = usuarios.union(usuarios_2) == usuarios | usuarios_2
eh_intersecao =usuarios.intersection(usuarios_2) == usuarios & usuarios_2
eh_difetente =usuarios.difference(usuarios_2) == usuarios - usuarios_2

# Dicionarios

dict_notes = {
    "Lucas" : 23,
    "Gabriel": 22,
    "Fulano": 11
}

print(dict_notes["Gabriel"])

user = {
    "name" : "Lucas",
    "age": 24,
    "admin": True,
    "endereço": {
        "rua" : "Av Edmundo Soares",
        "Bairro" : "Flores"
    }
}

print(user["endereço"])
print(user["endereço"]["rua"])

users = {
    "Lucas" : 23,
    "Gabriel": 22,
    "Fulano": 11
}


for user in users:
    print(users[user])

# users.keys()
# users.values()

for (k, v) in users.items():
    print(k, v)


# Challenge

user_str = input("Digite uma palavra: ")

looped_str = {}

for char_str in range(len(user_str)):
    print(user_str[char_str])
    count_times_char_str = 0
    if(user_str[char_str] != None):
      for aux_chat_str in range(len(user_str)):
          if(user_str[char_str] == user_str[aux_chat_str]):
              count_times_char_str +=1
      looped_str[user_str[char_str]] = count_times_char_str
  
print(looped_str)

# Funções

def bem_vindo(nome, idade, altura = 1.77):
    print("Olá, ", nome)
    print("Você tem", idade, "anos")
    print("Voce mede ", altura, "metros")

bem_vindo("Lucas Natan", 24)
# bem_vindo(nome = "Lucas Natan", idade = 24, altura = 1.77)

def calculadora(arg_1 = 0, arg_2 = 0):
    if(arg_1 == arg_2 == 0):
        return 2
    return arg_1 + arg_2

print(calculadora( 0, arg_2 =0))

# Desafio Funções

def eh_primo(n):
    i = 2
    while(i <= (n//2)):
        if(n % i == 0):
            return False
        i += 1
    return True
print(eh_primo(10))

def maior_posi_lista(list):
    bigger_posi = 0
    for i in range(len(list)):
        print(bigger_posi)
        if(list[i] > list[bigger_posi]):
            bigger_posi = i
    return (bigger_posi, list[bigger_posi])

lista = [1, 2, 55, 4, 5, -1, 222, 4]

print(maior_posi_lista(lista))

def maior_idade(pessoa):
    if(type(pessoa) == tuple):
      if(pessoa[1] >= 18):
        return "A pessoa é maior de idade"
      return "A pessoa é menor de idade"
    if(type(pessoa) == dict):
      if(pessoa["idade"] >= 18):
        return "A pessoa é maior de idade"  
      return "A pessoa é menor de idade"
        
print(maior_idade(("Lucas", 18)))
print(maior_idade({"nome":"Lucas", "idade": 17}))

def esta_na_lista(lista, item):
  for i in range(len(lista)):
    if(item == lista[i]):
      return True
  return False

lista_teste = [1, 2, 3, 4, 5]
print(esta_na_lista(lista = lista_teste, item = 6))

def fatorial(n):
  count_fat = 1
  if(n == 0 or n == 1):
    return 1
  else:
    for i in range(1, n + 1):
      count_fat *= i
  return count_fat

print(fatorial(5))