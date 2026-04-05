from rich import print

class Caneta:
    """
    selecione uma cor e a destampe para poder usar
    """
    def __init__(self, cor = ''):
        self.cor = cor.lower()
        self.tampa = False

    def destampar(self):
        self.tampa = True

    def tampar(self):
        self.tampa = False

    def quebraLinha(self, num):
        print( '\n' * num)

    def escrever(self, msg):
        if self.tampa == True:
            if self.cor == 'verde':
                print(f'[green]{msg}[/]', end=' ')
            elif self.cor == 'vermelho':
                print(f'[red]{msg}[/]', end=' ')
            elif self.cor == 'amarelo':
                print(f'[yellow]{msg}[/]', end=' ')
        else:
            print(f'\n\n\n[red]ERROR!!!! Você nao destampou a caneta')


c1 = Caneta("Vermelho")
c2 = Caneta('verde')
c3 = Caneta('AMARElo')

c1.destampar()
c2.destampar()
c3.destampar()


c1.escrever('Tem que aparecer vermelho')
c1.quebraLinha(2)
c2.escrever('Tem que escrever verde')
c3.escrever('Não posso aparecer')