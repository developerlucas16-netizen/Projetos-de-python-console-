# cire um programa que tenha uma tupla unica com nomes de produtos e seus respectivos preços. Depois disso, mostre uma listagem de preços, organizando os dados em forma de tabela.
produtos = (
    'Arroz', 5.50,
    'Feijão', 7.30,
    'Macarrão', 3.20,
    'Óleo', 4.80,
    'Açúcar', 2.90,
    'Café', 6.00,
    'Leite', 3.50,
    'Pão', 1.20,
    'Manteiga', 4.00,
    'Queijo', 8.50
)
print('Lista de Preços')
print('-' * 30)
for i in range(0, len(produtos), 2):
    nome = produtos[i]
    preco = produtos[i + 1]
    print(f'{nome:.<20} R$ {preco:>6.2f}')
