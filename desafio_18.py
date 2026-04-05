from rich import print, panel
from rich.panel import Panel

class Churrasco:
    """
    Calculo pratico para churrasco
    Levando em consideração:
    Consumo padrão: 400g por pessoa
    Preço: R$ 82,40/Kg
    """

    def __init__(self, title, quantidade):
        self.title = title
        self.quant = quantidade
        self.total_gramas = (quantidade * 400) / 1000
        self.preco = self.total_gramas * 82.40
        self.pagar = self.preco / quantidade

    def analisar(self):
        caixa = Panel(f'Analisando o [green]{self.title}[/] com [blue]{self.quant} convidados[/]\n'
        f'Cada participante comerá 0.4kg e cada Kg custa 82.40\n'
        f'Recomendo [blue]comprar {self.total_gramas:.3f}Kg[/] de carne\n'
        f'O custo total será de [green]R$ {self.preco:.2f}[/]\n'
        f'Cada pessoa pagará [yellow]R$ {self.pagar:.2f}[/] para participar.',
        title_align="center", title=self.title)
        print(caixa)


c1 = Churrasco('Churras dos amigos', 15)
c1.analisar()