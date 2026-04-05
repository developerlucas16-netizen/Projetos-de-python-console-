# Faça um jogo de par ou impar dentro de um loop infinito, 
# onde ele vai jogar contra a maquina
from random import randint
while True:
    jogador = int(input('Digite um numero: '))
    maquina = randint(0, 10)
    total = jogador + maquina
    tipo = ' '
    while tipo not in 'PI':
        tipo = input('Par ou Impar? [P/I] ').strip().upper()[0]
    print(f'Voce jogou {jogador} e a maquina {maquina}. Total de {total} ', end='')
    print('DEU PAR' if total % 2 == 0 else 'DEU IMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print('Voce VENCEU!')
        else:
            print('Voce PERDEU!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Voce VENCEU!')
        else:
            print('Voce PERDEU!')
            break
    print('Vamos jogar novamente...')