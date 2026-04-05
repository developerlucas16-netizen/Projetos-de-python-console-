# Peça 5 valores e guarde numa lista.
# mostre o maior e o menor com seu número de posição na lista.
valores = []
for i in range(5):
    valor = int(input(f'Digite o {i + 1}º valor: '))
    valores.append(valor)
print(f'\nO maior valor digitado foi {max(valores)} na posição {valores.index(max(valores))}')
print(f'O menor valor digitado foi {min(valores)} na posição {valores.index(min(valores))}')