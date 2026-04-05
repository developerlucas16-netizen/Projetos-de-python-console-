from rich import print
from rich.panel import Panel

class Produto:
    """
    Pegue o nome e o preço de um produto e cria uma etiqueta
    """

    def __init__(self, nome = '',preco = 0):
        self.nome = nome
        self.preco = preco

    def etiqueta(self):
        precof = f'R${self.preco:,.2f}'
        caixa = Panel(f"[white]{self.nome.center(30, ' ')}\n"
                      f"{'-' * 30}\n"
                      f"{precof.center(30, '.')}[/]",
        title="[white]Mensagem[/]", style="blue",width=34, title_align="center")
        print(caixa)


p1 = Produto('Iphone 17 Pro MAX', 25_000.85)
p2 = Produto('Notebook', 8_000)

p1.etiqueta()
p2.etiqueta()