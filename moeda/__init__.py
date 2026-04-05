def aumentar(num = 0, taxa = 0, formato = False):
  """
  -> num = é o valor que o usuario digitou.
  -> soma = é o valor que o usuario digitou + 15%.
  -> formato = Caso o valor de formato seja True ele ira passar o valor formatado em R$.
  """
  soma = (num * taxa/100) + num
  return soma if formato is False else moeda(soma)

def diminuir(num = 0, taxa = 0, formato = False):
  """
  -> num = é o valor que o usuario digitou.
  -> menos = é o valor - 15%.
  -> formato = Caso o valor de formato seja True ele ira passar o valor formatado em R$.
  """
  menos = num - (num * taxa/100)
  return menos if formato is False else moeda(menos)

def dobro(num = 0, formato = False):
  """
  -> num = é o valor digitado.
  -> vezes = o valor vezes 2.
  -> formato = Caso o valor de formato seja True ele ira passar o valor formatado em R$.
  """
  vezes = num * 2
  return vezes if formato is False else moeda(vezes)

def metade(num = 0, formato = False):
  """
  -> num = é o valor digitado.
  -> meio = é o valor pela metade.
  -> formato = Caso o valor de formato seja True ele ira passar o valor formatado em R$.
  """
  meio = num / 2
  return meio if formato is False else moeda(meio)

def moeda(preco = 0, moeda = 'R$'):
  """
  -> Aqui é apenas feito uma fortmatação para a moeda BR.
  """
  return f'{moeda}{preco:>.2f}'.replace('.',',')

def resumo(num = 0, ta = 0, td = 0):
  """
  -> num = é o valor digitado
  -> ta = taxa de aumento
  -> td = taxa de diminuir
  """
  
  preco = num
  vezes = dobro(num)
  meio = metade(num)
  aum = aumentar(num, ta)
  dim = diminuir(num,td)

  result = print(f"""
----------------------------
       RESUMO DO VALOR
----------------------------
Preço analisado:     {moeda(preco)}
Dobro do preço:      {moeda(vezes)}
Metade do preço:     {moeda(meio)}
{ta}% de aumento:      {moeda(aum)}
{td}% de redução:      {moeda(dim)}
""")

  return result


