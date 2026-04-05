def leiaDinheiro(msg):
  """
  -> msg = é o valor digitado.
  -> aqui transformamos o valor em string para fazer um fatiamento e após isso
  trocamos a , por um . para o python reconhecer.
  """
  valido = False
  while not valido:
    entrada = str(input(msg)).replace(',','.').strip()
    if entrada.isalpha() or entrada == '':
      print(f'\033[0;31mErro: \'{entrada}\' é um preço inválido!\033[m')
    else:
      valido = True
      return float(entrada)

def maior (* num, mostrar = True):
  """
  -> * num = mostra que o usuario pode passar varios numeros para analise
  """
  maior = 0
  cont = 0 

  for valor in num:
    if valor == maior:
      maior = valor
    elif valor > maior:
      maior = valor
    cont += 1

  if mostrar == True:
    print("\nAnalisando.....")
    print(f'Os valores foram')
    for valores in num:
      print(f"{valores}", end=' ')
    print(f', e o total foi de {cont}')
    print(f"E o maior foi o {maior}")
  else:
    return maior

def separar(lista):
  """
  -> lista = recebe o valor da lista de numeros que for passado
  """
  pares = list()
  impares = list()
  total_par = 0
  total_impar = 0
# E)
  for valor in lista:
    if valor % 2 == 0:
      pares.append(valor)
      total_par += valor
    elif valor % 2 != 0:
      impares.append(valor)
      total_impar += valor
  
  return pares, impares, total_par, total_impar

def vota(date):
  """
    date = data de nascimento
    idade calculo de idade da pessoa
    resp = resposta sobre a situação
  """

  idade = 2026 - date 

  if idade < 16:
    resp = "Negado"
    return resp
  elif idade == 16 or idade == 17:
    resp = "Opcional"
    return resp
  elif idade >= 18:
    resp = "Obrigatório"
    return resp

def ficha(nome = '<desconhecido>',gols=0):
  """
  -> nome = É o nome do jogador que o usuário digitar
  -> gols = e a quantidade de gols que ele fez 
  """
  if nome == "":
    nome = "<desconhecido>"

  frase = print(f"O nome do jogador é {nome} e ele fez {gols} gols na partidade")

  return frase

def leiaInt(frase):
  """
  frase -> mostra a frase digitada pelo usuário
  """

  while True:
    try:
      n = int(input(frase))
    except (ValueError, TypeError):
      print('\033[0;31mERRO: por favor um numero inteiro valido\033[m')
      continue
    except (KeyboardInterrupt):
      print('\n\033[3;31mEntrada de dados interrompida pelo usuario\033[m')
      return 0
    else: 
      return n
    
def leiaFloat(frase):
  """"
  -> Recebo o valor de frase e verifico se é inteiro
  """
  while True:
    try:
      n = float(input(frase))
    except (ValueError, TypeError):
      print('\033[0;31mERROR: por favor um numero real válido!!\033[m')
      continue
    except (KeyboardInterrupt):
      print('\033[0;31mO usuario preferiu não digitar o numero!\033[m')
      return 0
    else:
      return n


def notaAluno(* num, situação = False):
  """
  -> * num = mostra que ele vai passar várias notas 
  -> situação = mostra qual a situação do aluno conforme
  as nostas que forma passadas
  -> retorna os seguintes parêmntros:
    -> Maior nota
    -> menor nota
    -> Media
    -> Nota total
    -> Situação (opcional)
  """

  dados = dict()

  dados["total"] = len(num)
  dados["maior"] = max(num)
  dados["menor"] = min(num)
  dados["média"] = sum(num)/len(num)

  if situação == True:
    if dados["média"] >= 7:
      dados["situação"] = "Boa"
    elif dados["média"] >= 5:
      dados["situação"] = "Razoável"
    else:
      dados["situação"] = "Ruim"
  
  return dados
