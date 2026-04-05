# Faça uma função que encontre o maior valor indepentende de quantos foram informados

def maior (* num):
  maior = 0
  cont = 0 

  for valor in num:
    if valor == maior:
      maior = valor
    elif valor > maior:
      maior = valor
    cont += 1

  print("\nAnalisando.....")
  print(f'Os valores foram')
  for valores in num:
    print(f"{valores}", end=' ')
  print(f', e o total foi de {cont}')
  print(f"E o maior foi o {maior}")

  
  

maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()