# pedir 7 anos de nascimentos e mostrar quem e  + 18

cont_maior = 0
cont_menor = 0

for c in range(0,7):
    ano = int(input('Digite um ano de nascimento: '))
    idade = 2026 - ano
    if idade >= 18:
        cont_maior += 1
    else:
        cont_menor += 1

print(f'Tem {cont_maior} pessoas de maior, e {cont_menor} pessoas de menor')
