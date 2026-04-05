from rich import print
from rich import inspect

class Funcionario:
    """
    Permite criar uma forma de apresentção de novos funcionarios
    """
    def __init__(self, nome = '', setor = '', cargo = ''):
        self.nome = nome
        self.setor = setor
        self.cargo = cargo
        self.empresa = "Curso em Video"

    def apresentacao(self):
        return f':handshake: Óla, sou [blue]{self.nome}[/] e sou {self.cargo} do setor {self.setor} da empresa {self.empresa}'



c1 = Funcionario('Maria', 'Administração', 'Diretoria')
print(c1.apresentacao())
# inspect(c1, methods=True)

c2 = Funcionario('Pedro', 'TI', 'Programador')
print(c2.apresentacao())
# inspect(c2, methods=True)
