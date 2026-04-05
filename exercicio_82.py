# Crie um programa que vai ler varios numeros e colocar em uma lista.
# Crie duas listas extras para impar e par
# no final mostre as 3 listas

lista = []
lista_par = []
lista_impar = []

while(True):
  valor = int(input('Digite um valor: '))
  if valor not in lista:
    lista.append(valor)
    if valor % 2 == 0:
      lista_par.append(valor)
    else:
      lista_impar.append(valor)
    cont = str(input('\nQuer continuar? [S/N]')).upper()
    if cont == 'N':
      break
  
  else:
    print('\nEste numero já foi adicionado a lista..... tente outro')

print('-------lsita completa------')
for c_1, v_1 in enumerate(lista):
  print(f'indice -> {c_1} | valor -> {v_1}')
print('\n-----lista dos pares-----')
for c_2, v_2 in enumerate(lista_par):
  print(f'indice -> {c_2} | valor -> {v_2}')
print(f'\n---Lista dos impares----')
for c_3, v_3 in enumerate(lista_impar):
  print(f'indice -> {c_3} | valor -> {v_3}')