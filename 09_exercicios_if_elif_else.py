# %%
# Faça um programa que vende uma garrafa de água:
# Se o cliente escolher água mineral natural, será cobrado R$1,50
# Se o cliente escolher água mineral com gás, será cobrado R$2,50

texto = """
Escolha a água que deseja comprar:
(1) Água mineral natural
(2) Água mineral com gás
"""
escolha = input(texto)

conta = 0
if escolha == "1":
    conta = 1.5
elif escolha == "2":
    conta = 2.5

if conta == 0:
    print("Escolha uma valor correto para seu pedido!")
else:
    print("Sua conta é: R$", conta)

# %%
# Altere o programa anterior para 
# considerar a quantidade de garrafas de água

texto = """
Escolha a água que deseja comprar:
(1) Água mineral natural
(2) Água mineral com gás
"""
escolha = input(texto)

valor_item = 0
if escolha == "1":
    valor_item = 1.5
elif escolha == "2":
    valor_item = 2.5
    
if valor_item == 0:
    print("Escolha uma valor correto para seu pedido!")
else:
    qtde = input("Quantas garrafas você deseja?")
    qtde = int(qtde)
    valor_total = valor_item * qtde
    print("Sua conta deu um valor total de: R$", valor_total)