#Pedir largura e altura
#Medir a area
#Para cada 1L de tinta se pinta 2m²
#Faça o calculo de qunato de tinta vai gastar

h = float(input('Digite a altura: '))
l = float(input('Digite a largura'))
a = (l + h) * 2
t = a / 2

print(f'O valor da aréa a pintar é {a}m²')
print(f'E será necessário {t} litros de tinta')