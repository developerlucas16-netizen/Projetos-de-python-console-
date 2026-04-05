# Crie uma tupla preenchida com os 20 primeiros colocados da tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
# a) Os 5 primeiros colocados.  
# b) Os 4 últimos colocados.
# c) Uma lista com os times em ordem alfabética.
# d) Em que posição na tabela está o time da Chapecoense.
times = ('Atlético-MG', 'Palmeiras', 'Fluminense', 'Corinthians', 'Flamengo', 'Athletico-PR', 'Atlético-GO', 'Bragantino', 'Santos', 'São Paulo', 'Internacional', 'Ceará', 'Goiás', 'Botafogo', 'Coritiba', 'Fortaleza', 'Vasco da Gama', 'América-MG', 'Grêmio', 'Chapecoense')
print('Os 5 primeiros colocados são:')  
for i in range(5):
    print(f"{i+1}º - {times[i]}")
print('\nOs 4 últimos colocados são:')
for i in range(16, 20):
    print(f"{i+1}º - {times[i]}")
print('\nTimes em ordem alfabética:')
for time in sorted(times):
    print(time)
print(f'\nA Chapecoense está na {times.index("Chapecoense")+1}ª posição.')

