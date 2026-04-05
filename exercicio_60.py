# Calcule o fatorial de um numero

def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n - 1)
num = int(input("Digite um número para calcular o fatorial: "))
resultado = fatorial(num)
print(f'O fatorial de {num} é: {resultado}')
