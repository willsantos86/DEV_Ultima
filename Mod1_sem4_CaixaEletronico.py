'''
    Extra: https://dojopuzzles.com/problems/contando-moedas/
    DOJO: https://dojopuzzles.com/problems/caixa-eletronico/
    Desenvolva um programa que simule a entrega de notas quando um cliente efetuar um saque em um caixa eletrônico. Os requisitos básicos são os seguintes:
    Entregar o menor número de notas;
    É possível sacar o valor solicitado com as notas disponíveis;
    Saldo do cliente infinito;
    Quantidade de notas infinito (pode-se colocar um valor finito de cédulas para aumentar a dificuldade do problema);
    Notas disponíveis de R$ 100,00; R$ 50,00; R$ 20,00 e R$ 10,00
    Exemplos:
    Valor do Saque: R$ 30,00 - Resultado Esperado: Entregar 1 nota de R$20,00 e 1 nota de R$ 10,00.
    Valor do Saque: R$ 80,00 - Resultado Esperado: Entregar 1 nota de R$50,00 1 nota de R$ 20,00 e 1 nota de R$ 10,00.
'''

class CaixaEletronico:
    def __init__(self, nome):
        self.notas = [100, 50, 20, 10, 5]
        self.nome_banco = nome

    def sacar(self, valor_saque):
        valor = valor_saque
        resto = -1
        notas_entregues = []
        for valor_nota in self.notas:
            #   1        5        5     (teste de mesa, rastreio)
            qtd_notas = valor // valor_nota
            # 0       5      5      (teste de mesa, rastreio)
            resto = valor % valor_nota
            # 0     (teste de mesa, rastreio)
            valor = resto
            if qtd_notas > 0:
                notas_entregues.append(f'{qtd_notas} nota de R$ {valor_nota},00')

            # python debug bridge
            # import pdb; pdb.set_trace()
            # breakpoint()

        if resto == 0:
            self.imprimir_resultado(notas_entregues)
        else:
            print(f'Não é possível sacar o valor R$ {valor_saque},00')

        self.encerrar_atendimento()

    def encerrar_atendimento(self):
        print(f'Obrigado por usar o {self.nome_banco}')
    
    def imprimir_resultado(self, notas_entregues):
        print(', '.join(notas_entregues))


if __name__ == '__main__':
    caixa_eletronico = CaixaEletronico('Ultima Bank')
    valor = int(input('Valor do saque: '))
    caixa_eletronico.sacar(valor)