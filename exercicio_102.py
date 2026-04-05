# faça uma função chamada fatorial que receba 2 paremetros o numero a calcular e o o show 
# que é um valor logico(valor opcional) indicando se mostra ou nao o valor na tela

# A) Função fatorial
# B) dois paremtros num e show
# C) show e opcional
# D) calcular o fatorial 
# E) se nao for passado nada no show mostrar somente o resutado
# F) caso for passado algo no show mostrar o restutado completo passo a passo

def fatorial(num, show = False):
  """
  -> num: numero passado pelo usuario
  -> show: variavel de valor booleano, que mostra ou nao o passo a passo do fatorial
  -> fato: variavel para servir como resultado do fatorial
  """

  fato = 1
  for c in range(num, 0, -1):
    if show:
      print(f'{c}', end='')
      if c > 1:
        print(f' x ', end='')
      else:
        print(f' = ', end='')
    fato *= c
  print(fato, end='')
  return fato

num = int(input("Digite um numero para ver o fatorial: \n"))
mostrar = str(input("Voce deseja mostrar o passo a passo ? [S/N]")).upper()

if mostrar == "S":
  fatorial(num, show = True)

elif mostrar == "N":
  valor = fatorial(num)
  print(f"O valor do faorial de {num} é igual a {valor}")
