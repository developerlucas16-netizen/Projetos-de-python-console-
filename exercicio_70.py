# Faça um loop que simule um caixa
# pergunte o nome do produto e o preço
# quando o usuário digitar "sair" mostre o total da compra
# quantos produtos custando mais de 1000 reais
# qual produto mais barato  

total = 0
produtos_caro = 0
produto_barato = None
preco_barato = float('inf')
while True:
    nome_produto = input("Digite o nome do produto (ou 'sair' para finalizar): ")
    if nome_produto.lower() == 'sair':
        break
    preco_produto = float(input("Digite o preço do produto: "))
    
    total += preco_produto
    
    if preco_produto > 1000:
        produtos_caro += 1
        
    if preco_produto < preco_barato:
        preco_barato = preco_produto
        produto_barato = nome_produto
print(f"Total da compra: R${total:.2f}")
print(f"Quantidade de produtos custando mais de R$1000: {produtos_caro}")
if produto_barato is not None:
    print(f"Produto mais barato: {produto_barato} com preço de R${preco_barato:.2f}") 
