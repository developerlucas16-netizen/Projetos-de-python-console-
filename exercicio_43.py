# Desenvolva uma lógica IMC
# peça o peso e altura
# < 18.5 = Abaixo do peso
# 18.5 e 25: Peso ideal
# 25 até 30: sobrepeso
# 30 até 40: Obesidade
# >40: Obesidade morbida

peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))

imc = peso / (altura * altura)

if imc < 18.5:
    print(f'Abaixo do peso')

elif imc == 18.5 or imc < 25:
    print(f'Peso ideal')

elif imc == 25 or imc < 30:
    print(f'Sobrepeso')

elif imc == 30 or imc < 40:
    print(f'Obesidade')

else:
    print(f'Obesidade mórbida')
