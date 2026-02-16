def soma(a:float, b:float, *args)->float: # A e B são obrigatórios
    valores = [a,b] + list(args) # pode ser qualquer nome depois do asterisco
    return sum(valores)

def media(a:float, b:float, *args)->float:
    return soma(a,b, *args)/(len(args)+2)

a = float(input("Insira o valor de a: "))
b = float(input("Insira o valor de b: "))
c = float(input("Insira o valor de c: "))
d = float(input("Insira o valor de d: "))

print("Média:", media(a,b,c,d))