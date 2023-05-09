total = 0
continuar = 's'

while (continuar == 's'):
    valor = float(input("Entre com o valor da compra: "))
    total += valor
    continuar = input("Continar? [s/n] ")

print("Valor total da compra : ", total)
