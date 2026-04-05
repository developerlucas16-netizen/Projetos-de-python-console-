# faça um loop que simule um saque de dinheiro 
# mostrando quantas cedulas de cada valor serão necessárias para compor o valor total do saque
# considere as seguintes cedulas: 50, 20, 10, e 1
valor_saque = int(input("Digite o valor do saque: "))
cedulas = [50, 20, 10, 1]
for cedula in cedulas:
    quantidade_cedulas = valor_saque // cedula
    if quantidade_cedulas > 0:
        print(f"{quantidade_cedulas} cedula(s) de R${cedula}")
        valor_saque -= quantidade_cedulas * cedula  