# Faça programa que leia frase e diga se ela e um palindromo

frase = str(input('Digite a frase: '))

palavras = frase.split()
junto = ''.join(palavras)
inverso = ''

for letra in range(len(junto) - 1, - 1, - 1):
    inverso += junto[letra]

if inverso == junto:
    print(f'Temos um palíndromo')

else:
    print(f'Não é um polídromo')