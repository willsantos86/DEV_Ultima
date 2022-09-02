#Crie uma função que, ao receber um número inteiro, 
# retorna se um número  é par ou ímpar (utilizando **kwargs).

# %%
def par_impar(**num_int):

    if num_int['valor'] % 2 == 0: 
        return 'Par'
    else:
        return 'Impar'

#Programa Principal:
par_impar(valor= 3)