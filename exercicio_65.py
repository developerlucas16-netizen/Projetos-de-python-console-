cont = True
media = 0
quant = 0
maior = 0
menor = 999

while(cont):
  num = int(input('Digite um numero: '))
  continuar = str(input('Quer continuar ? [S/N] ')).lower()

  if continuar == 'S':
    media += num
    quant += 1
    if num > maior:
      maior = num
    elif num < menor:
      menor = num
  
  else:
    print(f'Voce digitou {quant} numeros e a média foi {media / quant:.2f}')
    print(f'O maior valor foi {maior} e o menor {menor}')
    break