# Crie um pequeno sistema de modularização
# que permita criar um cadastrar pessoas pelo seu nome e idade
# que permita cadastrar e listar

from exercicio_115.modulo import *
from exercicio_115.arquivo import *
from time import sleep

from myPacks.dados import leiaInt

arq = 'cursoemvideo.txt'

if not arquivoExiste(arq):
  criarArquivo(arq)
  sleep(2)
  limpar()

while True:
  resposta = menu(['Cadastrar nova Pessoa', 'Ver pessoas cadastradas', 'Sair do sistema'])
  if resposta == 1:
    limpar()
    # Opção de cadastrar uma nova pessoa
    cabeçalho('NOVO CADASTRO')
    nome = str(input('Nome: '))
    idade = leiaInt('Idade: ')
    cadastrar(arq, nome, idade)
    sleep(1)
    limpar()
  elif resposta == 2:
    limpar()
    # Opção de listar o conteudo do arquivo
    lerArquivo(arq)
  elif resposta == 3:
    limpar()
    cabeçalho('ATE LOGO')
    break
  else: 
    print('\033[0;31mERROR: por favor digite um valor válido!!\033[m')
    continue