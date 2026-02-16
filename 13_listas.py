# %%
idades = [28, 42, 43, 50, 60, 80, 18, 71, 36]

print(idades)

# %%

nome = ["Leandro", "de Mello", 24, "Solteiro", 700]
print(nome)

type(nome)

# %%
print(nome[4])

# %%
idades = [28, 42, 43, 50, 60, 80, 18, 71, 36]
print(sum(idades))
print(len(idades))
print(sum(idades)/len(idades))
print(min(idades))
print(max(idades))

# %%
lista = ["Lendro de Mello", 24, True, "Solteiro", ["Robert", "Matheus"], ["Estagiário", "Auxiliar de Lab Químico", "Analista de Dados Jr."]]
print(len(lista))
print(lista[4][0])
print(lista[len(lista)-1][1])

# %%
print(lista[-2][-1])

# %%
print(lista[0:5])
print(lista[:3]) # pegando do primeiro até terceiro item da lista
print(lista[4][0:2])
print(lista[4][-2:]) # pegando do ultimo até o final
#  start : stop

# %%
lista = ["Lendro de Mello", 24, True, "Solteiro", ["Robert", "Matheus"], ["Estagiário", "Auxiliar de Lab Químico", "Analista de Dados Jr."]]
cargos = lista[5][:: -1] # vai do inicio da lista e até o final da lista, e vai indo de trás pra frente
print(cargos)

# start : stop : step
# começa : para : de quanto em quanto anda

