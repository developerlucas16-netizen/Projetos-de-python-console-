# Faça uma PA sendo 
# A) de 1 até 10 de 1 em 1
# B) de 10 até 0 de 2 em 2
# C) personalizada
# D) Na pesolazida tem que ter como fazer de forma decrescente
# E) De forma nomral
# F) Caso o passo for zero considerar como 1
# G) Caso o passo for negativo considerar como positivo e descerscente

from time import sleep

def contador():
  print('~' * 30)
  print('         Contador         ')
  print('~' * 30)

  # A)
  for c in range(1, 11, 1):
    print(c, end=' ')
  print()
  
  print('~' * 30)

  # B) 
  for c in range(10, 0, -2):
    print(c, end=' ')
  print()

  print('~' * 30)

  # C)
  inicio = int(input('Inicio: '))
  fim = int(input('Fim:      '))
  razao = int(input('Razão:   '))

  print('~' * 30)

  if razao > 0 and inicio > fim:
    for c in range (inicio, fim, razao):
      print(c, end=" ")
    print()

  # D) 
  elif razao > 0 and inicio < fim:
    razao *= -1
    for c in range(inicio, fim, razao):
      print(c, end=" ")
    print()
  
  # F)
  elif razao == 0:
    razao = 1
    for c in range(inicio, fim, razao):
      print(c, end=" ")
    print()


contador()