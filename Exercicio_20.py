# Faça um programa para sortear os nomes
import random

n1 = str(input('Digite o nome do primero aluno: '))
n2 = str(input('Digite o nome do segundo aluno: '))
n3 = str(input('Digite o nome do terceiro aluno: '))
n4 = str(input('Digite o nome do quarto aluno: '))

nomes = [n1, n2, n3, n4]

random.shuffle(nomes)

print(f'O escolhido foi {nomes}')