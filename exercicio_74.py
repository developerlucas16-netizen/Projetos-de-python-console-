# Crie um programa que vai gerar 5 numeros aleatorios e colocar em uma tupla. Depois disso, mostre a listagem de numeros gerados e indique o menor e o maior valor que estão na tupla.  
from random import randint
numeros = (randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100))
print(f'Os números gerados foram: {numeros}')
print(f'O menor valor é: {min(numeros)}')
print(f'O maior valor é: {max(numeros)}') 