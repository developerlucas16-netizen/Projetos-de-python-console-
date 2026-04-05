# faça um modulo chamado moeda.py que tenha as funções
  # aumentar()
  # diminuir()
  # dobra()
  # metade()

from myPacks import moeda

num = float(input("Digite o numero: "))

print(f'O valor {moeda.moeda(num)} + 15% é {moeda.moeda(moeda.aumentar(num))}')
print(f'O valor {moeda.moeda(num)} - 15% é {moeda.moeda(moeda.diminuir(num))}')
print(f'O valor {moeda.moeda(num)} x 2 é {moeda.moeda(moeda.dobro(num))}')
print(f'O valor {moeda.moeda(num)} / 2 é {moeda.moeda(moeda.metade(num))}')