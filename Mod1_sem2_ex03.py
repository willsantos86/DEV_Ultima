'''A recepção de um nave espacial recebe as pessoas com uma mensagem de boas vindas 
de acordo com o nome que elas forneceram ao fazer o cadastro na recepção. 
Crie uma aplicação que imprima a mensagem de boas vindas de acordo com a lista de nomes na 
#ista: nomes = [‘Elysson’, ‘Giulia’, ‘Willian’, ‘Gileno’] com a seguinte mensagem 
“Bem vindo, NOME_PESSOA!! Seja bem vindo a nave Imperial dos Siths.”. 
Crie um programa que faça a interpolação da string de boas vindas, substituindo o NOME_PESSOA 
pelo nome lido da lista e imprimindo a frase de boas vindas com o nome substituindo.'''

nomes = ['Elysson', 'Giulia', 'Willian', 'Gileno']

for nome in nomes:
    print(f'Bem vindo, {nome}!!\n Seja bem vindo a nave Imperial dos Siths.')
    print('-='*20)