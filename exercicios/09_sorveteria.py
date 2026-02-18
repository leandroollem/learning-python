# Faça o programa de uma sorveteria, onde o usuário pode escolher:
# Tipo de sorvete: casquinha (R$1,00), cascão (R$2,50), cestinha (R$4,00)
# Sabor do sorvete: morango, creme, chocolate
# Cobertura: Caramelo (R$1,50), morango (R$1,50), chocolate (R$1,50), sem cobertura (R$0,00)
# Apresente o valor a ser pago

tipo = input("Qual tipo de sorvete deseja: (1) Casquinha | (2) Cascão | (3) Cestinha ")
sabor = input("Qual sabor de sorvete deseja: (1) Morango | (2) Creme | (3) Chocolate ")
cobertura = input("Qual cobertura deseja: (1) Caramelo | (2) Morango | (3) Chocolate | (4) Sem cobertura ")

valor_conta = 0

if tipo == "1":
    valor_conta += 1
elif tipo == "2":
    valor_conta += 2.5
elif tipo == "3":
    valor_conta += 4
else:
    print("Insira um valor válido.")

if cobertura in ["1","2","3"]:
    valor_conta += 1.5
else:
    print("Insira um valor válido.")

print("O valor da conta é: R$", valor_conta)