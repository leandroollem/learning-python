# Altere o programa anterior para considerar a quantidade de garrafas de água

produto = input("Escolha seu tipo de água: (1) Água Mineral Natural | (2) Água Mineral com Gás ")
qtde_item = float(input("Insira a quantidade de garrafas: "))

valor_item = 0
if produto == "1":
    valor_item = 1.5
elif produto == "2":
     valor_item = 2.5
else:
    print("Insira um valor de produto válido")

valor_total = valor_item * qtde_item
print("O valor total é: R$", valor_total)