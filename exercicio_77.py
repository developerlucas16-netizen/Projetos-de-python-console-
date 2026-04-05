# crie um programa que tenha uma tupla com várias palavras (nao pode usar acentos)
# depois disso voce deve mostrar para cada palavra quais sao as suas vogais
palavras = ('python', 'programacao', 'exercicio', 'tupla', 'vogais')
for palavra in palavras:
    print(f'\nNa palavra {palavra.upper()} temos as vogais: ', end='')
    for letra in palavra:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')

