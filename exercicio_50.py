# Peça 6 numeros
# separes entre impar e pares
# Some somentes os pares
total = 0
cont = 0


for c in range(0,6):
    num = int(input('Digite um numero: '))
    if num % 2 == 0:
        total += num
        cont += 1
  
    
print(f'Você digitou {cont} numeros pares, cujo a soma foi {total}')
    
