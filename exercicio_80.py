# cire um programa que peça 5 numeros para uma lista
# depois mostre a lista ordenada sem usar o metodo sort()
numeros = []
for i in range(5):
    numero = int(input("Digite um número: "))
    numeros.append(numero)
# Ordenar a lista usando o método de ordenação por seleção
for i in range(len(numeros)):
    min_index = i
    for j in range(i + 1, len(numeros)):
        if numeros[j] < numeros[min_index]:
            min_index = j
    # Trocar o elemento atual com o elemento mínimo encontrado
    numeros[i], numeros[min_index] = numeros[min_index], numeros[i]
print("Lista ordenada:", numeros)
