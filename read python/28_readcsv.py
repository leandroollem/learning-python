# %% 
arquivo = "data.csv"

with open(arquivo) as open_file:
    data = open_file.readlines()
print(data)

# %%
for linha in data:
    print(linha)
# %%
# separando pela ";"
dados = dict()

chaves = data[0].strip("\n").split(";") #tirando o \n das strings
chaves

for c in chaves:
    dados[c] = []

# %%
for l in data[1:]:
    valores = l.strip("\n").split(";")
    for i in range(0, len(valores)):
        dados[chaves[i]].append(valores[i])
dados


# %%
idades = []
for i in dados["idade"]:
    idades.append(int(i))
media = sum(idades)/len(idades)
media
# %%
