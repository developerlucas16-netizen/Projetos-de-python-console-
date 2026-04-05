from rich import print
from rich.table import Table

tabela = Table(title="Tabela de Preços", width=45)

tabela.add_column("Nome", justify="center", style="cyan", no_wrap=True)
tabela.add_column("Preço", justify="center", style="cyan", no_wrap=True)
tabela.add_row("lápis", "R$1,50")
tabela.add_row("borracha", "R$3,50")

print(tabela)