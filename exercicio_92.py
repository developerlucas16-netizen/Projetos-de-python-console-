# Crie um programa que leia nome ano de nascimento e carteira de trabalho e cadastre com idade
# caso carteira de trabalho for != 0 deverá ter
# ano de contratação
# salário
# aposentadoria

import os

def limpar():
    os.system('cls' if os.name == 'nt' else 'clear')

pessoa = dict()

pessoa['nome'] = str(input('Digite seu nome: ')).capitalize()
pessoa['sexo'] = str(input('Digite seu sexo M ou F: ')).upper()
data = int(input('Digite seu ano de nascimento: '))
idade = 2026 - data
pessoa['idade'] = idade
pessoa['carteira'] = int(input('Digite o numero da sua carteira [0 para caso não tenha]: '))

if pessoa['carteira'] == 0:
  limpar()
  print('-------------------------------------')
  print('---------------Casdastro-------------')
  print('-------------------------------------')
  for k, v in pessoa.items():
    print(f'{k}: {v}')
else:
  pessoa['ano de contratação'] = int(input('Digite o ano que você começou a trabalhar: '))
  pessoa['salario'] = float(input('Digite o seu salario: '))
  if pessoa['sexo'] == "F":
    pessoa['aposentadoria'] = data + 62
  elif pessoa['sexo'] == 'M':
    pessoa['aposentadoria'] = data + 65
    
  limpar()
  print('-------------------------------------')
  print('---------------Casdastro-------------')
  print('-------------------------------------')
  for k, v in pessoa.items():
    print(f'{k}: {v}')
