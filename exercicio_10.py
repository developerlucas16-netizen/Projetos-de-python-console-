#Peça umm valor em reais
#Converta em dolar, euro

real = float(input('Digite qunato você tem na carteira: R$'))

dolar = 5.15
euro = 6.08

if (real < 100.00) :
    print(f'Vishhh, ta meio pobre mas ok, seu valor convetido é de:')
    print(f'Em dolar seria = U${real / dolar:.2f}')
    print(f'Em euro seria = E${real / euro:.2f}')

elif (real >= 100 or real < 5000) :
    print(f'Bom bom, já ta melhor que muito gente, seu valor convetido é de:')
    print(f'Em dolar seria = U${real / dolar:.2f}')
    print(f'Em euro seria = E${real / euro:.2f}')

else :
    print(f'Beleza o Elon Musk, seu valor convetido é de:')
    print(f'Em dolar seria = U${real / dolar:.2f}')
    print(f'Em euro seria = E${real / euro:.2f}')