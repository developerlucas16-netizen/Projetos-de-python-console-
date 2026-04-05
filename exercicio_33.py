# Ler 3 numeros e mmostrar qual o maior e o menor

num_1 = int(input('Me fale o primeiro numero: '))
num_2 = int(input('Me fale o segundo numero:'))
num_3 = int(input('Me fale o terceiro numero: '))

maior = 0
menor = 0

if num_1 > num_2 and num_1 > num_3:
    maior = num_1   
elif num_2 > num_1 and num_2 > num_3:
    maior = num_2
else:
    maior = num_3

if num_1 < num_2 and num_1 < num_3:
    menor = num_1
elif num_2 < num_1 and num_2 < num_3:
    menor = num_2
else:
    menor = num_3

print(f'''
Os numeros foram {num_1}, {num_2}, {num_3}
e o maior é o {maior}
e o menor e o {menor}
''')
