from exercicio_115.modulo import *

def arquivoExiste(nome):
  try:
    a = open(nome, 'rt')
    a.close()
  except FileNotFoundError:
    return False
  else: 
    return True

def criarArquivo(nome):
  try:
    a = open(nome, 'wt+')
    a.close()
  except:
    print('ERROR!!!')
  else:
    print(f'Arquivo {nome} criado com sucesso!')
  
def lerArquivo(nome):
  try: 
    a = open(nome, 'rt') 
  except:
    print('ERROR!!!')
  else:
    limpar()
    cabeçalho('PESSOAS CADASTRADAS')
    for linha in a:
      dado = linha.split(';')
      dado[1] = dado[1].replace('\n', '')
      print(f'{dado[0]:<30} {dado[1]:>3} anos')
    sleep(10)
    limpar()

def cadastrar(arq, nome = 'desconhecido', idade = 0):
  try:
    a = open(arq, 'at')
  except:
    print('\033[0;31mERROR!!!\033[m')
  else:
    try:
      a.write(f'{nome};{idade}\n')
    except:
      print('\033[0;31mHouve um erro na hora de cadastrar\033[m')
    else:
      print(f'\033[0;32mCadastro da pessoa {nome} feito com sucesso!!!\033[m')