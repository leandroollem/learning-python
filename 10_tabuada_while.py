# %%
numero = 2
count = 0

while count <= 20:
    print(numero, "x", count, "=", numero * count)
    count += 1 # Mesma coisa que count = count + 1
print("Finalizado!")

# %%
# Quais são os numeros diviseis por 4 num intervalo de 4 a 100

count = 4
while count <= 100:
    resto = count % 4
    if resto == 0:
        print(count)
    count += 1
