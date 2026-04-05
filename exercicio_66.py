# Faça um while que peça numeros e caso for parar digitar 999
# somar todos os numeros digitados e mostrar a soma
soma = 0  
while True:
    numero = int(input("Digite um número (ou 999 para parar): "))
    if numero == 999:
        break
    soma += numero
print(f"A soma dos números digitados é: {soma}")  