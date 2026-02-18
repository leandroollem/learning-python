# Faça um programa que receba 4 alturas usando um laço de repetição e realize a soma dessas alturas.

soma_altura = 0
for i in range(4):
    altura = float(input("Insira a altura: "))
    soma_altura += altura
print(f"A soma das altura é {soma_altura}")