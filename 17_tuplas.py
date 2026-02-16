# %%
dados_lista = [32, 1, "Oi", "Sabugo", True]
dados_lista

# %%
dados_lista.append(1000)
dados_lista

# %%
tupla_lista = (32, 1, "Oi", "Sabugo", True, ["Roberto", "Matheus", "Diego"])
print(type(tupla_lista))
print(tupla_lista)

# TUPLA É IMUTÁVEL. LISTAS QUE NÃO PODEM SER ALTERADAS

# %%
# Mas da para alterar LISTAS dentro de TUPLAS
tupla_lista[-1].append("Guilherme")

# %%
tupla_lista