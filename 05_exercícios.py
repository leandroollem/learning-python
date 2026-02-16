# 01. Bom dia.
print("Bom dia!")

# 02. Bom dia com nome da pessoa.
nome = input("Bom dia! Qual seu nome? ")
print("Que prazer te conhecer,", nome)

# %%
# 03. Crie uma história simples.
#  Adicione essa história em um programa. 
# A cada parágrafo, a história deve aguardar o usuário apertar “enter”
# para dar continuidade.

p1 = "Era uma vez."
p2 = "Bem no comecinho da história."
p3 = "Na verdade, não tem história alguma."

input(p1)
input(p2)
input(p3)

# %%
# Faça um programa que receba um número inteiro e 
# calcule sua raiz quadrada e exiba o resultado.
número = int(input("Insira um número inteiro e te direi sua raiz quadradra"))
raiz = número ** 0.5
print("A raiz quadrada de", número, "é:", raiz)

# %%
# Faça um programa que exiba o dobro de um número 
# inserido pelo usuário.

numero = int(input("Insira um número e te direi o dobro dele"))
dobro = numero * 2
print("O dobro de", numero, "é:", dobro)