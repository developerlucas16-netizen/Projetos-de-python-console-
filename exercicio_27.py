# Peça o nome completo de uma pessoa e mostre:
# O primeiro nome
# O último nome

nome = str(input('Digite seu nome completo: '))
nome = nome.strip()
print(f'''
Primeiro nome: {nome.split()[0]}   
Último nome: {nome.split()[-1]}     
''')