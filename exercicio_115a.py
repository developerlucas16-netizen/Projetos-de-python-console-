# Crie um pequeno sistema de modularização
# que permita criar um cadastrar pessoas pelo seu nome e idade
# que permita cadastrar e listar

from myPacks import cadPessoas as cp

while True:
  resposta = cp.menu(['Cadastrar nova Pessoa', 'Ver pessoas cadastradas', 'Sair do sistema'])
  try:
    if resposta == 1:
      nome = str(input('Digite seu nome: '))
      idade = int(input('Digite sua idade: '))
      resp = cp.cadastrar(nome, idade)
      print(resp)
      cp.sleep(2)
      cp.limpar()
      continue
    elif resposta == 2:
      cp.listar()
      continue
    elif resposta == 3:
      cp.limpar()
      cp.cabeçalho("SAINDO DO ISTEMA... ATÉ")
      break
    else: 
      print('\033[0;31mERROR: por favor digite um valor válido!!\033[m')
      continue
  except (TypeError, ValueError):
    print('\033[0;31mERROR: por favor digite um valor válido!!\033[m')
    cp.sleep(2)
    cp.limpar()
    continue
  except (KeyboardInterrupt):
    print('\033[0;31mValor nao informado!!\033[m')
    cp.sleep(2)
    cp.limpar
    continue