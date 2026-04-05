# Faça um programa que peça a média de um aluno
# De acordo com a media informe a situção
# coloque tudo em um diacionario
# Mostre o dicionario

import os

def limpar():
    os.system('cls' if os.name == 'nt' else 'clear')


aluno = dict()
classe = list() 

while(True):
  aluno['nome'] = (str(input('Digite o nome do aluno: ')))
  aluno['media'] = float(input('Digite a média: '))

  if aluno['media'] <= 4:
    aluno['situacao'] = 'reprovado'
  elif aluno['media'] <= 7: 
    aluno['situacao'] = 'recuperação'
  elif aluno['media'] > 7:
    aluno['situacao'] = 'aprovado'
  classe.append(aluno.copy())

  cont = str(input('Deseja continuar [S/N]: ')).upper()
  if cont == 'S':
    limpar()
  elif cont == 'N':
    break

for c in classe:
  for k, v in aluno.items():
    print(f'{k} -> {v}', end='|')
  print()