# Solicite ao usuário o nome de uma fruta e exiba o preço correspondente.

# %%
fruta = input("Insira o nome da fruta que gostaria de saber o preço")
frutas = {
"Maçã":"R$1,50",
"Banana":"R$2,75",
"Uva":"R$1,90",
"Pera":"R$1,25",
"Laranja":"R$0,65",
"Limão":"R$1,25",
"Goiaba":"R$2,15",
"Abacaxi":"R$3,20",
"Jaca":"R$5,80"
}

if fruta in frutas:
    print(frutas[fruta])
else:
    print("Entre com um nome de fruta válido")

# %% 
# Escreva um programa que solicite ao usuário frases. Para parar de solicitar frases, 
# ele pode apenas apertar o “enter”.
# Seu programa deve apresentar cada frase e quantas vezes ela foi repetida.


dados = {}
while True:
    frase = input("Insira uma frase")
    if frase == "":
        break
    if frase not in dados:
        dados[frase] = 1
    else:
        dados[frase] += 1

for i,j in dados.items(): # Ou for i in dados:
    print(i, "->", j) # print(i, "->", dados[i])

items = list(dados.items()) # transforma em lista
items.sort(key=lambda x: x[-1], reverse=True) #ordenando usando uma função
for i, j in items:
    print(i, "->", j)