cont = True
total = 0
quant = 0

while(cont):
  num = int(input('Digite um numero [999 para parar]: '))

  if num != 999:
    total += num
    quant += 1
  
  elif num == 999:
    print(f'Você digitou {quant} numeros cujo a soma é {total}')
    break