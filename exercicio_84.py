# Faça um programa que leia o nome e o peso de várias pessoas e guarde tudo em uma lista
# A) quantas pessoas foram cadastradas
# B) uma listagem com pessoas mais pessadas
# C) uma listagem com as pessoas mais leves

dados = list()
pessoas = list()
maior = menor = 0

while(True):
  nome = str(input("Digite seu nome: "))
  dados.append(nome)
  peso = float(input('Digite o seu peso: '))
  dados.append(peso)
  if len(pessoas) == 0:
    maior = menor = dados[1]
  else:
    if dados[1] > maior:
      maior = dados[1]
    elif dados[1] < menor:
      menor = dados[1]
  pessoas.append(dados[:])
  dados.clear()
  seguir = str(input('Deseja continuar? [S/N]: ')).upper()
  if seguir != 'S':
    break

print('-=' * 30)
print(f'Ao todo, você cadastrou {len(pessoas)} pessoas.')
print(f'O maior peso foi o de {maior}Kg. Peso de ', end=' ')
for c in pessoas:
  if c[1] == maior:
    print(f' {c[0]} ', end=' ')
print()
print(f'O menor peso foi o de {menor}Kg. Peso de ', end=' ')
for p in pessoas:
  if p[1] == menor:
    print(f' {p[0]} ', end=' ')
print()