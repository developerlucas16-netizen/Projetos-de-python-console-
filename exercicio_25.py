# Verificar se ter ferreira dentro do nome pedido

name = str(input('Digite seu nome completo: '))

name.title()
verify = name.find('Ferreira')

if verify >= 0:
    print(f'Sim seu nome tem Ferreira')

else:
    print(f'Seu nome nao tem Ferreira')