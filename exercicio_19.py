# Faça um programa para sortear um nome
import random

n1 = str(input('Digite o nome do primero aluno: '))
n2 = str(input('Digite o nome do segundo aluno: '))
n3 = str(input('Digite o nome do terceiro aluno: '))
n4 = str(input('Digite o nome do quarto aluno: '))

nomes = [n1, n2, n3, n4]

print(f'O escolhido foi {random.choice(nomes)}')