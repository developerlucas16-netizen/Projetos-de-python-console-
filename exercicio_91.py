# fazer 4 jogadores pegarem 1 numero aleatorio de 1 a 6
from random import randint
from time import sleep
from operator import itemgetter

jogo = {'jogador_1': randint(1,6),
        'jogador_2': randint(1,6),
        'jogador_3': randint(1,6),
        'jogador_4': randint(1,6)}

ranking = dict()

print('Valores sorteados: ')
for k, v in jogo.items():
  print(f'{k} tirou {v} no dado.')
  sleep(1)

randint = sorted(jogo.item(), key=itemgetter(1), reverse=True)
print(ranking)




