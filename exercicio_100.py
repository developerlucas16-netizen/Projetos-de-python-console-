# Faça um função que sorteie 5 numeros
# Faça uma função que o mostre os numeros pares e os somem

# A) importar biblioteca random
# B) criar uma função aonde sortea 5 numeros de 1 a 100
# C) criar uma função que le os numeros sorteados 
# D) mostrar quais sao impares e quais sao pares 
# E) somar todos os impares e todos os pares 
# F) mostrar os impares separados 
# G) mostrar os pares separados 

# A) 
from random import randint

# B)
def sortear():
  from random import randint
  numeros = list()
  numeros.append(randint(0, 100))
  numeros.append(randint(0, 100))
  numeros.append(randint(0, 100))
  numeros.append(randint(0, 100))
  numeros.append(randint(0, 100))
# C)
  print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
  print("Este são os valores sorteados:")
  print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
  for valor in numeros:
    print(f'{valor}', end='->')
  print()
  print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
  separar(numeros)

# D)
def separar(lista):
  pares = list()
  impares = list()
  total_par = 0
  total_impar = 0
# E)
  for valor in lista:
    if valor % 2 == 0:
      pares.append(valor)
      total_par += valor
    elif valor % 2 != 0:
      impares.append(valor)
      total_impar += valor
# F)
  print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
  print("      Esses são os impares       ")
  print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
  for i in impares:
    print(f"{i}", end="->")
  print()
  print(f"O valor somado de todos os impares são {total_impar}")

  print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
  print("       Esses são os pares        ")
  print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
  for p in pares:
    print(f"{p}", end="->")
  print()
  print(f"O valor somado de todos os impares são {total_par}")
    
sortear()
