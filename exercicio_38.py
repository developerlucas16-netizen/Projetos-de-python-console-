# Peça dois numeros
# Veja se o primeiro e maior
# ou o segundo
# ou se são iguais

num_1 = int(input('Digite o primeiro: '))
num_2 = int(input('Digite o segundo: '))

if num_1 > num_2:
    print('O 1º numero e maior')

elif num_2 > num_1:
    print('O 2º numero e maior')

elif num_1 == num_2:
    print('Os numeros são iguais')