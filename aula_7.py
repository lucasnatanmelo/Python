# Receber input

idade = input("Digite sua idade: ")

# Transform to int
idade = int(idade)

print("A idade digitada é: ", idade)

# Exercícios

valor_compra = float(input("Digite o valor da compra"))

valor_frete = float(input("Digite o valor do frete"))

leitura_cliente = str(input("Cliente possui cadastro?"))

recebe_desconto = ((leitura_cliente == 's') or (
    (valor_compra + valor_frete) > 100.00))

print("Receberá o desconto: ", recebe_desconto)
