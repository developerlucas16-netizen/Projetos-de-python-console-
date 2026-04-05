from rich import print
from rich.panel import Panel

from myPacks.limpeza import limpar


class TV:
    def __init__(self):
        self.esc = None
        self.tv = False
        self.volume = 2
        self.canal = 1

    def desligada(self):
        tele_Desligada = Panel(f' :prohibited: [red]A TV está desligada',
        title_align="center",
        title='[ TV:tv: ]',
        width=40)

        print(tele_Desligada)

    def ligada(self):
        tele_ligada = Panel(f' CANAL = [white on yellow] 1 [/] 2 3 4 5\n'
        f' VOLUME = [white on cyan]    [/][white on white]      [/]',
        title_align="center",
        title='[ TV:tv: ]',
        width=40
        )
        print(tele_ligada)

    def escolha(self):
        self.esc = str(input(f'< CH{self.canal} >   - VOL{self.volume} +    '))
        if self.esc != 0:
            return self.esc
        else:
            self.esc = 0
            return self.esc

    def trocarCanal(self):
        try:
            if self.esc == '>' and self.canal != 5:
                self.canal += 1
            elif self.esc == '<' and self.canal != 1:
                self.canal -= 1
        except:
            pass
        else:
            ch =''
            opc = self.canal
            for c in range(1, 6):
                if c == opc:
                    ch += f'[white on yellow] {c} [/]'
                else:
                    ch += f' {c}'
            return ch
        return None

    def trocarVolume(self):
        if self.esc == '+' and self.volume != 5:
            self.volume += 1
        elif self.esc == '-' and self.volume != 1:
            self.volume -= 1

        esc = self.volume

        if esc == 1:
            return f'[white on cyan]  [/][white on white]        [/]'
        elif esc == 2:
            return f'[white on cyan]    [/][white on white]      [/]'
        elif esc == 3:
             return f'[white on cyan]      [/][white on white]    [/]'
        elif esc == 4:
            return f'[white on cyan]        [/][white on white]  [/]'
        elif esc == 5:
            return f'[white on cyan]          [/][white on white][/]'


    def aposMudar(self):
        tele_apos = Panel(f' CANAL = {self.trocarCanal()}\n'
        f' VOLUME = {self.trocarVolume()}\n',
        title_align="center",
        title='[ TV:tv: ]',
        width=40
        )
        print(tele_apos)



tv = TV()
tv.desligada()

while True:
    esc = tv.escolha()

    if esc == '@':
        limpar()
        tv.ligada()

    elif esc == '>':
        limpar()
        tv.aposMudar()

    elif esc == '<':
        limpar()
        tv.aposMudar()

    elif esc == '-':
        limpar()
        tv.aposMudar()

    elif esc == '+':
        limpar()
        tv.aposMudar()

    elif esc == '0':
        limpar()
        tv.desligada()
        break