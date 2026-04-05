# Pergunte a idade
# e pela idade coloque se ele vai alistar 
# Se ja era pra estar alistado
# ou se ja passou da idade de se alistar

idade = int(input('Digite sua idade: '))

if idade < 18:
    print(f'Ainda não precisa se alistar')

elif idade == 18:
    print(f'hora de se alistar')

elif idade > 18:
    print(f'Ja passou da hora de se alistar')