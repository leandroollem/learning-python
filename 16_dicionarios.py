# %%

lista = [1, 2, 3, 6, 7, "ds", "dr", "ty", True]
lista [2]

# %%
# pares de chave/valor
# uma chave corresponde a um valor

dados_lista = {
    "nome":"Lendro",
    "sobrenome":"Mello",
    "Formação":["Técnico em Edificações", "Técnologo em Processos Químicos"],
    "Escolas":["Etec", "Fatec"],
    "Amigos":[
        {"nome":"Robert","cargo":"designer"},
        {"nome":"Matheus","cargo":"estudante"}
    ] 
}
print(dados_lista)

# %%
# As chaves podem ser do tipo STRING,INTEIRO e FLOAT(não recomendável)
print(dados_lista["nome"])
print(dados_lista["Formação"][-1])
print(dados_lista["Amigos"][-1]["cargo"])

# %%
# Adicionando mais uma chave no dicionário
dados_lista["Estado Civil"] = "Solteiro"
print(dados_lista)

# %%
print(dados_lista.keys()) # Mostra a lista de chaves que podemos acessar
print(dados_lista.values()) # Mostra os valores do par Chave e Valor
print(dados_lista.items()) # Mostra os pares Chave e Valor

# %%
for i in dados_lista:
    print(i, ":", dados_lista[i])

# %%
for chave, valor in dados_lista.items():
    print(chave, ":", valor)

# %%
