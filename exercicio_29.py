# Escreva um progrma que leia a velocidade de um carro
# Se ele ultrapassar 80km, mostre uma mensagem dizendo que ele foi multado
# o valor da multa e 7 reais a cada km a cima do limite

real_value = int(input('Digite a velocidade registrada no radar: '))

value_fine = (real_value - 80) * 7

if real_value > 80:
    print(f'O carro ultrapassou o limite de velocidade, a multa é de R${value_fine:.2f}')

else:
    print('O carro está dentro do limite de velocidade, continue dirigindo com segurança!')