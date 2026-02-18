# Faça um programa que conte quantas vezes a letra “a” aparece em uma palavra

palavra = input("Insira uma palavra: ")
count = 0

for i in palavra:
    if i == "a":
        count +=1

print(count)