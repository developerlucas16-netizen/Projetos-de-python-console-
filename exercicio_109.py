# faça um modulo chamado moeda.py que tenha as funções
  # aumentar()
  # diminuir()
  # dobra()
  # metade()

from myPacks import moeda

num = float(input("Digite o numero: "))

print(f'O valor {moeda.moeda(num)} + 13% é {moeda.aumentar(num, 13, True)}')
print(f'O valor {moeda.moeda(num)} - 10% é {moeda.diminuir(num, 10, True)}')
print(f'O valor {moeda.moeda(num)} x 02  é {moeda.dobro(num, True)}')
print(f'O valor {moeda.moeda(num)} / 02  é {moeda.metade(num, True)}')