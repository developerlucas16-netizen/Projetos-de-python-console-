# faça uma progressão aritimética com pausa e perguntando quanto termos o usuário quer mostrar
print('Gerador de PA')  
print('-=' * 10)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
termo = primeiro
cont = 1
while cont <= 10:
    print(f'{termo} -> ', end='')
    termo += razao
    cont += 1
print('PAUSA')
mais = int(input('Quantos termos você quer mostrar a mais? '))
total = cont + mais
while cont <= total:
    print(f'{termo} -> ', end='')
    termo += razao
    cont += 1
    print('FIM')