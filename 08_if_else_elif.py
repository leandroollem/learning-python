# %%
idade = 18

if idade >= 18:
    print("Você pode beber cerveja!")
if idade < 18:
    print("Você não pode beber cerveja!")

# %%
idade = 12

if idade >= 18:
    print("Você pode beber cerveja!")
else:
    print("Você não pode beber cerveja!")

# %% 
idade = 17

if idade >= 70:
    print("Cuidado com a bebida")
elif idade >= 18:
    print("Você pode beber cerveja!")
elif idade == 17:
    print("Ainda não pode beber cerveja!")
else:
    print("Você não pode beber cerveja!")