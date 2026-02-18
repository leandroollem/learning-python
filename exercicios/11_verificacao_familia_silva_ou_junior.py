nome = input("Insira seu nome completo: ")
nome_split = nome.lower().split(" ") # separa cada parte do nome com espaços

if "junior" in nome_split: # Roberto Junior -> ["Roberto", "Junior"] 
    print("Você é um Junior.")
if "silva" in nome_split: # Silvana Correventos -> ["Silvana", "Correventos"]
    print("Você é um Silva.") 
if "junior" not in nome_split and "silva" not in nome_split:
    print("Você não é um Junior, nem Silva.")
