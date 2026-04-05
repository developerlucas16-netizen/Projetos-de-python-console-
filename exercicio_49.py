# Mostrar a tabuado com o numero escolhido pelo usario

num = int(input('Digite o numero para ver a tabuada: '))
num_2 = 1

for c in range(0, 11):
    print(f'{num} x {c} = {c * num}')