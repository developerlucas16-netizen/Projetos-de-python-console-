# Escreva um programa pra aprovar o emprestimo bancario paa a compr de uma casa.
# Pergunte o valor da casa
# O salrio
# E em quantos anos
# A prestação não pode exceder 30% do salario 
# Se exceder será negado

salario = float(input('Digite o valor do seu salario: '))
valor_casa = float(input('Digite o valor da casa: '))
anos = int(input('Em quantos anos você irá pagar: '))

porcentagem = salario * 0.3

prestacao = valor_casa / anos

if prestacao < porcentagem:
    print(f'Parabens seu emprestimo foi consedido!!!')

elif prestacao > porcentagem:
    print(f'Desculpe mais não posso liberar')