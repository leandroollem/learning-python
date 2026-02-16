# %%
# Faça um programa que receba 4 alturas usando 
# um laço de repetição e realize a soma dessas alturas.

soma = 0
count = 4
while count > 0:
    altura = float(input("Insira a altura: "))
    soma += altura
    count -= 1
print("A soma das alturas inseridas é:", soma)

# %%
# Faça um programa que receba uma quantidade indefinida de valores 
# correspondentes a “saldo em conta”, mas quando o usuário apertar
# “enter” sem digitar valor algum, o programa para de receber valores,
# e exibe a soma de todos os valores digitados anteriormente.

saldo_total = 0
while True:
    saldo = input("Insira o saldo: ")
    if saldo == "":
        break
    else:
        saldo_total += float(saldo)
print("O saldo total é:", saldo_total)
