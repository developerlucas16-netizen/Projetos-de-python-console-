# Pedir KM percorrido
# Quantidade de dias alugados
# Calcular o preço total a pagar
# dia = 60
# Km rodado = 0,15

print(f'---------Aluguel de carros--------')
dias = int(input('Por quantos dias você iria ficar com o carro?  '))
km = float(input('Qunatos km você rodou: '))

preco_dias = dias * 60
preco_km = km * 0.15
preco_total = preco_km + preco_dias

print(f'Você ficou com o carro durante {dias} dias e rodou {km}km')
print(f'O preço dos dias e dos km respectivamente ficou em R${preco_dias} e R${preco_km}')
print(f'Ficou no valor total de R${preco_total}')
print(f'----------------------------------')

