# Faça um programa que receba um número. Verifique se o número 
# informado é par ou ímpar. Exiba o resultado da seguinte maneira:
# 	O número x é impar
# ou
# 	O número x é par

def par_impar(numero:int)->str:
    if numero % 2 == 0:
        return "par"
    else:
        return "impar"
numero = int(input("Insira um número: "))
resultado = par_impar(numero)
print("O valor", numero, "é:", resultado)
