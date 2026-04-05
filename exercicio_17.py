# Faça um porgrama que calcule a hipotenusa


cat_adj = float(input('Qual o valor do cateto adjecente: '))
cat_opt = float(input('Qual o valor do cateto oposto: '))

hipotenusa = (cat_opt ** 2 + cat_adj ** 2) ** (1/2)

print(f'A valor dos catetos:')
print(f'Cateto adjacente: {cat_adj}')
print(f'Cateto oposto: {cat_opt}')
print(f'Portanto a hipotenusa é {hipotenusa}')