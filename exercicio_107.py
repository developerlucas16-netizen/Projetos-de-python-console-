# faça um modulo chamado moeda.py que tenha as funções
  # aumentar()
  # diminuir()
  # dobra()
  # metade()

from myPacks import moeda

num = int(input("Digite o numero: "))

print(f'O valor {num} + 15% é {moeda.aumentar(num)}')
print(f'O valor {num} - 15% é {moeda.diminuir(num)}')
print(f'O valor {num} x 2 é {moeda.dobro(num)}')
print(f'O valor {num} / 2 é {moeda.metade(num)}')