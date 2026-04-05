# Faça um programa que mostre se o numero e primo

num = int(input("Digite um numero: "))
if num < 2:
    print("O numero deve ser maior ou igual a 2.")
else:
    primo = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            primo = False
            break
    if primo:
        print(f"{num} é um número primo.")
    else:
        print(f"{num} não é um número primo.")
    
