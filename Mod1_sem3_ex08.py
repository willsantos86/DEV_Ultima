def prefixo(palavra_1,palavra_2):
    # Verificar se aprimeira palavra é prefixo da segunda palavra.
    if palavra_1 == palavra_2.split()[0][:2]:
        print('Palavra é prefixo')
    else:
        print('Não é prefixo')
    return


#Programa Principal:
prefixo('uf','ufabc')