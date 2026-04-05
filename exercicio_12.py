# Pedir um preço
# Mostrar esse produto com preço antigo e com 5% de desconto

produto = float(input('Digite o valor de um produto: '))

desconto = ( - produto * 0.05) + produto

print(f'O produto está R${produto}, e com o desconto de 5% sai por R${desconto}')
