from rich import print
from rich.panel import Panel


def mostrar():
    pass


class Gamer:
    """
    Pega o nome, o nick e os jogos que a pessoa gosta
    depois os mostra em um painel
    """

    def __init__(self, name = '', nick = ''):
        self.name = name
        self.nick = nick
        self.fav = list()

    def add_favoritos(self, name):
        self.fav.append(name)

    def mostrar(self):
        return f'\n'.join(f':video_game: [blue]{j}[/]' for j in self.fav)

    def ficha(self):
        caixa = Panel(f'Nome real: [black as blue]{self.name}[/]\n'
        f'Jogos favoritos:'
        f'\n{self.mostrar()}',
        title_align="center", title=f"Jogador <{self.nick}>")

        print(caixa)


j1 = Gamer('Lucas Alcantara', 'Levisabo')
j1.add_favoritos('Valorant')
j1.add_favoritos('God of War')
j1.add_favoritos('Minecraft')
j1.add_favoritos('Fifa 24')

j1.ficha()