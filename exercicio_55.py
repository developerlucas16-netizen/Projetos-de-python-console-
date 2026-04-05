# Peça 5 valores de peso
# e mostre qual o maior e menor

menor = 0
maior = 0

for p in range(1,6):
    peso = float(input(f"Digite o peso da {p}ª pessoa: "))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

print(f'''
O maior peso lido foi o de {maior:.2f}Kg
O menor peso lido foi o de {menor:.2f}Kg
''')