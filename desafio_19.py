from rich import print
from time import sleep

class Livro:
    """
    Criar um livro com título e podendo avançar páginas
    """

    def __init__(self, title = '', pag = 0):
        self.title = title
        self.pag = pag
        self.pag_atual = 1
        print(f':open_book:[blue] Você acabou de abrir o livro[/] [red]{self.title}[/][blue]'
              f' que tem [/][green]{self.pag} páginas[/][blue] no total. Você agora está na [/]'
              f'[yellow]página {self.pag_atual}[/]')

    def avancar_paginas(self, ler = 0):
        if self.pag_atual + ler < self.pag:
            for _ in range(ler):
                print(f'Pág{self.pag_atual}  :play_button: ', end='')
                sleep(1)
                self.pag_atual += 1
            print(f'[blue]Você avançou {ler} páginas e agr está na página [/][yellow]{self.pag_atual}[/]')
        else:
            print(f'FIM do livro')


li = Livro('10 coisas que eu aprendi', 20)
li.avancar_paginas(5)
li.avancar_paginas(10)
