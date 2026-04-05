# Verifique se o ano e biseexto

year = int(input('Qual o ano? '))

if year % 4 == 0:
    print(f'Sim, {year} é um ano bissexto')

else:
    print(f'Não, {year} não é um ano bissexto')