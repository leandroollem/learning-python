# %%
nome = "Lendro"

for letra in nome:
    print(letra)

# %%
numero = 2
max_numero = 100

for i in range(1, max_numero+1):
    print(numero, "x", i, "=", numero*i)

# %%
for i in range(4, 101):
    if i%4 == 0:
        print(i)

# %%
# Faça um programa que receba 4 alturas usando 
# um laço de repetição e realize a soma dessas alturas.
count = 4
for i in range(count):
    altura = input("Entre com a altura:")
    altura = float(altura)
    soma+= altura
print("Soma das altura é:", soma)