# Aprimore o desafio 86, mostrando no final:
# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.
matriz = [[], [], []]
soma_pares = 0
soma_terceira_coluna = 0  
for i in range(3):
    for j in range(3):
        valor = int(input(f'Digite um valor para [{i}, {j}]: '))
        matriz[i].append(valor)
        if valor % 2 == 0:
            soma_pares += valor
        if j == 2:
            soma_terceira_coluna += valor
maior_segunda_linha = max(matriz[1])
print('-=' * 30)
for i in range(3):
    for j in range(3):
        print(f'[{matriz[i][j]:^5}]', end='')
    print()
print('-=' * 30)
print(f'A soma de todos os valores pares digitados é: {soma_pares}')
print(f'A soma dos valores da terceira coluna é: {soma_terceira_coluna}')
print(f'O maior valor da segunda linha é: {maior_segunda_linha}')

