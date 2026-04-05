# Criar um programa que verfique qual o salario atual
# Se for > 1.250,00 o aumento vai ser de 10%
# Se for <= 1.250,00 o aumento vai ser de 15%

salario = int(input('Digite o valor do seu salário: '))

if salario > 1250:
    aumento = (salario * 0.10) + salario
    print(f'O seu salario é R${salario}, portanto com o reajuste agora é R${aumento}')

elif salario <= 1250:
    aumento = (salario * 0.15) + salario
    print(f'O seu salario é R${salario}, portanto com o reajuste agora é R${aumento}')