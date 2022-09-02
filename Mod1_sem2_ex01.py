# Crie uma aplicação que calcule a quantidade de reais (R$) que o Sr.
# João possui moedas no caixa. A aplicação deve imprimir o valor total em reais (R$), 
# pode-se utilizar ponto flutuante para poder representar o valor com duas casas decimais 
# no momento que for imprimir na tela o valor.


#Moeda         | Quantidade
#--------------|-------------
#5 centavos    |     35
#10 centavos   |     50
#25 centavos   |     30
#50 centavos   |     15
#1 real        |     19




c_5 = float(input('Quantidade de moedas de R$0.05 '))
c_10 = float(input('Quantidade de moedas de R$0.10 '))
c_25 = float(input('Quantidade de moedas de R$0.25 '))
c_50 = float(input('Quantidade de moedas de R$0.50 '))
c_1 = float(input('Quantidade de moedas de R$1.00 '))

cinco_centavos = 0.05 * c_5
dez_centavos = 0.10 * c_10
vinte_cinco_centavos = 0.20 * c_25
cinquenta_centavos = 0.50 * c_50
um_real = 1 * c_1

total_valor = cinco_centavos + dez_centavos + vinte_cinco_centavos + cinquenta_centavos + um_real

print(f'O valor total em reais do Sr. João é: R$ {total_valor}')