# Faça um loop que cadastre o nome e o sexo da pessoa, e a cada nova pessoa perguntar se o usuario quer continuar
# No final mostre quantas pessoas foram cadastradas, quantos homens e quantas mulheres
# quantas pessoas com mais de 18 anos foram cadastradas   
total_pessoas = 0
total_homens = 0
total_mulheres = 0
total_maiores_18 = 0
while True:
    nome = input('Digite o nome da pessoa: ')
    sexo = input('Digite o sexo da pessoa (M/F): ').upper()
    idade = int(input('Digite a idade da pessoa: '))
    total_pessoas += 1
    if sexo == 'M':
        total_homens += 1
    elif sexo == 'F':
        total_mulheres += 1
    if idade > 18:
        total_maiores_18 += 1
    continuar = input('Deseja continuar? (S/N): ').upper()
    if continuar == 'N':
        break
print(f'Total de pessoas cadastradas: {total_pessoas}')
print(f'Total de homens cadastrados: {total_homens}') 
print(f'Total de mulheres cadastradas: {total_mulheres}')
print(f'Total de pessoas com mais de 18 anos cadastradas: {total_maiores_18}')
