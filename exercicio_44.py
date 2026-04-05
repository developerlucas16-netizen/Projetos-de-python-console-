# Caulcule o valor a ser pago
# considerando a forma de pagamento
# dinhiero/cheque = 10% de desconto
# a vista no debito = 5% de desconto
# 2x no cartao = preço normal
# 3x ou mais 20% de juros

preco = float(input('Digite o valor do produto: '))
print('''
Escolha sua forma de pagamento
    1 -> dinheiro ou cheque
    2 -> debito ou credito a vista
    3 -> credito 2x
    4 -> credito 3x
''')
pagamento = int(input('Digite a escolha: '))

match pagamento:
    case 1:
        dinheiro = preco - (preco * 0.1)
        print(f'O preço a pagar será R${dinheiro:.2f}')
    
    case 2: 
        debito = preco - (preco * 0.05)
        print(f'O preço a pagar será R${debito:.2f}')
    
    case 3: 
        credito_2x = preco 
        print(f'O preço a pagar será R${credito_2x:.2f}')
    
    case 4:
        credito_3x = preco + (preco * 0.2)
        print(f'O preço a pagar será R${credito_3x:.2f}')