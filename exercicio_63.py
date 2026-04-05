# Mostre a sequencia de fibonnaci perguntando ao usuario quantos numeros ele quer mostrar

def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=' ')
        a, b = b, a + b 
quantidade = int(input("Quantos números da sequência de Fibonacci você quer mostrar? "))
fibonacci(quantidade) 
