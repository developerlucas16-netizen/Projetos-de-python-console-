# Faça um programa que ajude um jogador da Mega Sena a criar palpites. O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
from random import sample
print('Gerador de Palpites para a Mega Sena')
quantidade = int(input('Quantos jogos você quer que eu sorteie? '))
palpites = []
for c in range(quantidade):
    jogo = sample(range(1, 61), 6)
    palpites.append(jogo)
print('-=' * 3, f'SORTEANDO {quantidade} JOGOS', '-=' * 3)
for i, jogo in enumerate(palpites):
    print(f'Jogo {i + 1}: {sorted(jogo)}')
    