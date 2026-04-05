# Peça o nome de um jogador 
# Pergunte quantas partidas ele jogou
# pergunte quantos gols ele fez em cada partida
# some o total de gols

jogador = dict()
gols = list()
total = 0

jogador['nome'] = str(input('Nome do jogador: '))
partidas = int(input(f'Quantas partidas o {jogador["nome"]} jogou? '))

for c in range(0, partidas):
  gol = int(input(f'Quantos gols na partida {c}: '))
  gols.append(gol)
  total += gol

print('-=' * 20)

jogador['gols'] = gols.copy()
jogador['total'] = total

print(jogador)

print('-=' * 20)

for k, v in jogador.items():
  print(f'O campo {k} tem o valor {v}')

print('-=' * 20)

cont = 0

print(f'O jogador {jogador['nome']} jogou {partidas} partidas:')
for c in gols:
  print(f'=> na partida {cont}, fez {c} gols.')
  cont += 1

print(f'O total de gols foi {jogador['total']}')