# faça uma função que le um numero e te mostre qual foi
# faça com validação de dados

def leiaInt(frase):
  """
  frase -> mostra a frase digitada pelo usuário
  """
  valor = 0
  num = str(input(frase))
  
  ok = False

  while(True):
    if num.isnumeric():
      valor = int(num)
      ok = True
    else:
      print("\033[31mERROR !!!! por favor digite um numero !!!\033[31m")
    if ok == True:
      break
  return valor
  


n = leiaInt("Digite um numero: ")
print(f'Você achou o numero {n}')


