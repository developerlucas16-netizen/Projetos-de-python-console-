# crie um programa que o usuario possa adicionar quantos numeros ele quiser
# verifique se o numero já foi adicionado a lista
# No final mostre todos em ordem crescente

lista = []

while(True):
  valor = int(input('Digite um valor: '))
  if valor not in lista:
    lista.append(valor)
    cont = str(input('Quer continuar? [S/N]')).upper()
    if cont == 'N':
      break
  
  else:
    print('Este numero já foi adicionado a lista..... tente outro')

lista.sort()

for c, v in enumerate(lista):
  print(f'\nindice {c}|valor -> {v}')

