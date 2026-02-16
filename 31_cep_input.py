import requests

cep = input("Insira um CEP: ")

url = "https://viacep.com.br/ws/{cep}/json"

response = requests.get(url.format(cep=cep))

if response.status_code == 200:
    dados = (response.json())
for chave, valor in dados.items():
    print(chave, "->", valor)