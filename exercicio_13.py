#Pedir o salario
#Mostrar o salario e o aumento de 15%

salario = float(input('Qual o salario? '))

aumento = (salario * 0.15) + salario

print(f'O seu salario atual e de R${salario}')
print(f'O o seu aumento foi no valor de R${salario * 0.15}')
print(f'Portanto seu novo salario e no valor de R${aumento}')