# Faça um programa que calcule o preço de viagem por km
# sendo que até 200km cada km e 0,50 e é 0,45km

distance  = int(input('Digite quantos KM serao percorridos nessa viagem: '))

if distance <= 200:
    total = distance * 0.50
    print(f'O valor final para viajar {distance}km será de R${total:.2f}')

elif distance > 200:
    total  = distance * 0.45
    print(f'O valor final para viajar {distance}km será de R${total:.2f}')