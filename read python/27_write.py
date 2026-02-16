# %% 
txt = "Nova linha2\n"
nome_arquivo = "Outra_história.txt"

with open(nome_arquivo, mode="a") as open_file:
    open_file.write(txt)
# %%
