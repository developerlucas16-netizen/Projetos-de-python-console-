def area(l, c):
  """"
  -> l = representa a largura
  -> c = representa o comprimento
  -> area = é o calculo de largura vezes comprimento
  """
  area = l * c
  print(f'A largura é {l:.2f}mts e o comprimento {c:.2f}, portanto a area é {area}mts²')


from time import sleep

def contador(i = 0, f = 10, r = 1):
  """
  -> i = Representa o inicio da PA.
  -> f = Representa o fim da PA.
  -> r = Representa o razao da PA.
  """
  print('~' * 30)
  print('         Contador         ')
  print('~' * 30)

  inicio = i
  fim = f
  razao = r

  print('~' * 30)

  if razao > 0 and inicio > fim:
    for c in range (inicio, fim, razao):
      print(c, end=" ")
    print()

  elif razao > 0 and inicio < fim:
    razao *= -1
    for c in range(inicio, fim, razao):
      print(c, end=" ")
    print()
  
  elif razao == 0:
    razao = 1
    for c in range(inicio, fim, razao):
      print(c, end=" ")
    print()

def sortear():
  """
  -> sorteia 5 numeros e coloca em uma lista
  """
  from random import randint
  numeros = list()
  numeros.append(randint(0, 100))
  numeros.append(randint(0, 100))
  numeros.append(randint(0, 100))
  numeros.append(randint(0, 100))
  numeros.append(randint(0, 100))

  return numeros

def fatorial(num, show = False):
  """
  -> num: numero passado pelo usuario
  -> show: variavel de valor booleano, que mostra ou nao o passo a passo do fatorial
  -> fato: variavel para servir como resultado do fatorial
  """

  fato = 1
  for c in range(num, 0, -1):
    if show:
      print(f'{c}', end='')
      if c > 1:
        print(f' x ', end='')
      else:
        print(f' = ', end='')
    fato *= c
  print(fato, end='')
  return fato