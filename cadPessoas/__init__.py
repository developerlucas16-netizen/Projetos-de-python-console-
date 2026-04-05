import os
from myPacks import dados

def limpar():
    os.system('cls' if os.name == 'nt' else 'clear')

from time import sleep

pessoa = dict()
grupo = list()

def cadastrar(nome = '<desconhecido>', idade = 0):
  """
  -> nome = nome cadastrado
  -> idade = idade cadastrada
  """
  pessoa["nome"] = nome
  pessoa["idade"] = idade

  frase = "Cadastro concluido!!!!"

  grupo.append(pessoa.copy())

  limpar()

  return frase

def listar():
  limpar()
  linha()
  cabeçalho("CADASTRO DE PESSOAS")
  linha()
  for c in grupo:
    for v, k in c.items():
      print(f'{v} = {k}', end=' | ')
    print()
  sleep(8)
  limpar()


def linha(tam = 42):
  return '-' * tam

def cabeçalho(txt):
  print(linha())
  print(txt.center(42))
  print(linha())

def menu(lista):
  cabeçalho("MENU PRINCIPAL")
  c = 1
  for item in lista:
    print(f'\033[33m{c}\033[m -> \033[34m{item}\033[m')
    c += 1 
  linha()
  opc = dados.leiaInt('Sua opção: ')

  return opc