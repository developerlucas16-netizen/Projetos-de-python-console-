# Peça o nome de um jogador 
# Pergunte quantas partidas ele jogou
# pergunte quantos gols ele fez em cada partida
# some o total de gols

import os


def limpar():
    os.system('cls' if os.name == 'nt' else 'clear')


time = list()
jogador = dict()
gols = list()
total = 0
cont = 0
cod = 0

while(True):
  jogador['nome'] = str(input('Nome do jogador: '))
  partidas = int(input(f'Quantas partidas o {jogador["nome"]} jogou? '))

  for c in range(0, partidas):
    gol = int(input(f'Quantos gols na partida {c}: '))
    gols.append(gol)
    total += gol

  print('-=' * 20)

  jogador['gols'] = gols.copy()
  jogador['total'] = total
  time.append(jogador.copy())
  
  continuar = str(input('Quer continuar? [S/N] ')).upper()
  if continuar == 'S':
    limpar()
  elif continuar == 'N':
    limpar()
    print('-=' * 30)
    print('cod  Nome         gols             Total')
    print('----------------------------------------')
    for l in time:
      for j in jogador.values():
        print(f'{cod} {j}', end=' ')
        cod += 1
    print( )

    print('Mostrar dados de qual jogador? (999 para parar)')
    opcao = int(input('Digite a sua opção: '))

    if opcao >= 0:
      print(f'-- Levantamento do jogador {time[opcao['nome']]}')
      for c in time[jogador['gols']]:
        print(f'=> na partida {cont}, fez {c} gols.')
        cont += 1
    elif opcao == 999:
      break
