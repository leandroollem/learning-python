# %%
# métodos = ações

idades = []
while True:
    idade = input("Insira a idade: ")
    if idade == "":
        break
    idades.append(int(idade))
print(idades)
media = sum(idades)/len(idades)
minimo = min(idades)
maximo = max(idades)
qtde = len(idades) 

print("Média:",media)
print("Mínimo:",minimo)
print("Máximo:",maximo)
print("Quantidade de elementos na lista:",qtde) 