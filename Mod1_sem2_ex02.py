'''Um freelancer está com dificuldade para calcular qual o valor cobrar por um projeto
que está estimado em 80 horas. Após pensar e revisitar o preço de alguns projetos
que cobrou no passado ele montou a seguinte fórmula: 
valor inicial + quantidade de horas estimadas * valor da hora + 15% do valor calculado. 
Sua tarefa é criar um programa que faça essa conta para o freelancer. 
Considere que o valor inicial sempre será 1000,00 R$ e o valor da hora cobrada é de 20,45 R$. 
A aplicação deve imprimir o valor calculado pelo projeto considerando duas casas decimais na formatação 
do valor. Dica: Olhar a ordem como as operações da fórmula devem ser realizadas.'''


valor_inicial = 1000
qtd_horas_est = 80
valor_da_hora = 20.45
estimado = qtd_horas_est * valor_da_hora
total = (valor_inicial + estimado) * 1.15

print(f'O valor total do projeto é: R$ {total}')