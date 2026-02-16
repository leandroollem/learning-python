# Funções que ja vem no python, implementadas por alguém:
# print()
# input()
# sum()
# len()
# max()
# min()

# Implementando uma função no Python
# %%
def f(x):
    resultado = 1 + x
    return resultado #retornar um valor a algo, parecido com o input 

# %%
f(10)
# %%
# Adicionar os TypesHints é importante
def juros_compostos(aporte:int, taxa:float, anos:int)->float:
    '''juros_compostos serve para calcular o retorno financeiro a partir de um aporte.   
    Deve-se considerar o valor, a taxa de juros atual e o tempo (em anos) para o cálculo do valor a ser retornado.  
    
    aporte:  
        um número inteiro, que representa o valor em R$.  

    taxa:  
        um número float entre 0 e 1 que representa  o valor da taxa de juros.  

    anos:  
        um número inteiro >= 1, que representa a quantidade de anos que o investimento terá liquidez.  
    '''
    juros = aporte * (1+taxa) ** anos
    return juros


# %%
juros_compostos(1000, 0.13, 4)
# %%
juros_compostos(aporte=1000, taxa=0.13, anos=4)
# %%
juros_compostos(anos=4,aporte=1000,taxa=0.13)

# %%
