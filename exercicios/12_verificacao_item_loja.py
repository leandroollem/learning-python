# Faça um programa que verifique se o item que a pessoa escolheu para comprar na loja está na lista: 
# laranja, cerveja, miojo, carvão, picanha.

escolha = input("Escreva um item: ").lower()
items = "laranja cerveja miojo carvão picanha"

if escolha in items:
    print("Seu item existe!")
else:
    print("Escolha um item existente.")