# Fazer um while que peça um valor e mostre a tabuada desse valor
# Caso o valor for negativo o progrma deve para
while True:
    valor = int(input('Digite um valor para ver a tabuada: '))
    if valor < 0:
        print('Programa encerrado!')
        break
    print(f'Tabuada do {valor}:')
    for i in range(1, 11):
        print(f'{valor} x {i} = {valor * i}')
