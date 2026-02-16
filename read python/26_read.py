# %%
nome_arquivo = "historia.txt"

#Jeito que não há necessidade de fechar, fecha automaticamente
with open(nome_arquivo) as open_file:
    conteudo = open_file.read()
print(conteudo)

# __________

# Tem a necessidade de fechar

# open_file = open(nome_arquivo)

# conteudo = open_file.read()
# print(conteudo)

# open_file.close()
