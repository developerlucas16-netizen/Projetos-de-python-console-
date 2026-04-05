# Faça um programa que mostre o seno, coseno e tangente de um angulo
import math

angulo = float(input('Digite o valor do angulo: '))

tangente = math.tan(math.radians(angulo))
coseno = math.cos(math.radians(angulo))
seno = math.sin(math.radians(angulo))

print(f'O valor do angulo foi {angulo}')
print(f'Tangente: {tangente}')
print(f'Coseno: {coseno}')
print(f'Seno: {seno}')