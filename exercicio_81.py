# Crie um programa que vai ler varios numeros e colocar numa lista.
# a) qunatos numeros foram digitados.
# b) a lista de forma descresente
# c) se o valor 5 está na lista

lista = []

while(True):
  valor = int(input('Digite um valor: '))
  if valor not in lista:
    lista.append(valor)
    cont = str(input('Quer continuar? [S/N] ')).upper()
    if cont == 'N':
      break
  
  else:
    print('Este numero já foi adicionado a lista..... tente outro')

print(f'\nForma digitados {len(lista)} numeros')

lista.sort(reverse=True)
for c, v in enumerate(lista):
  print(f'\nindice -> {c}|valor -> {v}')

if 5 in lista:
  print(f'\nFoi encontrado o valor 5 na lista')

elif 5 not in lista:
  print(f'\nO valor 5 não foi encontrado na lista')