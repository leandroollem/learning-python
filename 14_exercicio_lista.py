# %%
# Faça um programa que recebe uma lista de numeros
# do usuario e conte quantas vezes um numero
# específico aparece na lista
# Solicite ao usuario um numero e exiba a contagem

lista = [1,2,2,2,3,5,9,6,7,8,3,5,4,5,2,2]

numero = int(input("Insira um número para contar an lista: "))
contador = 0
for i in lista:
    if i == numero:
        contador += 1
print("Quantidade de", numero, "na lista é:", contador)