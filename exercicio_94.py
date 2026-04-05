# crie um programa que peça nome idade e sexo de varias pessoas.
# A) qunatas pessoas cadastradas
# B) Uma lista com mulheres
# C) uma lista com a idade acima da média

import os

def limpar():
    os.system('cls' if os.name == 'nt' else 'clear')

pessoas = dict()
grupo = list()
cont = 0
total_idade = 0

while(True):
  print('-=' * 20)
  print('               Cadastro       ')
  print('-=' * 20)
  pessoas['nome'] = str(input('Nome: '))
  idade = int(input('Idade: '))
  if idade == int:
    total_idade += idade
    pessoas['idade'] = idade
  else:
    print('ERROR!!! por favor digite o valor correto')
  sexo = str(input('M ou F')).upper()
  if sexo == 'M' or sexo == 'F':
    pessoas['sexo'] = sexo
    grupo.append(pessoas.copy())
    cont += 1
  else:
    print('ERROR!!! por favor digite o valor correto')
  continuar = str(input('Deseja continuar [S/N]')).upper()
  if continuar == 'N':
    break
    limpar()
  else:
    limpar()
    
media = idade / cont

print('-=' * 20)
print('               Cadastro       ')
print('-=' * 20)
print(f'A) Ao temos {cont} pessoas cadastradas!!!')
print(f'B) A média de idade é de {media:.2f} anos.')
print(f'C) As mulheres cadastradas foram ',end='')
for p in grupo:
  if p['sexo'] in 'F':
    print(f'{p['nome']}', end='')
  print()
print(f'D) Lista das pessoas que estão acima da média:')
for c in grupo:
  if c['idade'] >= media:
    print('   ')
    for k, v in c.items():
      print(f'{k} = {v}; ', end='')
    print()
print('<<-=-ENCERRADO-=->>')