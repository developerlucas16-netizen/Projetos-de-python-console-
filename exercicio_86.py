# Crie um programa que crie uma matriz 3x3 e preencha ela com valores lidos no teclado. No final, mostre a matriz na tela, com a formatação correta..  
matriz = []
for i in range(3):
    linha = []
    for j in range(3):
        valor = int(input(f"Digite o valor para a posição [{i}][{j}]: "))
        linha.append(valor)
    matriz.append(linha)
print("Matriz 3x3:")
for linha in matriz:
    print(linha)