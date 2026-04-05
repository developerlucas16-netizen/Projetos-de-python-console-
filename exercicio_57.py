# Peça o sexo de uma pessoa
# E mostre uma mensagem de erro caso nao for M ou F

cont = True

while(cont):
  sexo = str(input('Digite o sexo [M/F]: '))
  sexo.lower()

  if sexo == 'm' or sexo == 'f':
    print(f'Sexo {sexo} registrado com sucesso!')
    break
  
  else:
    print('Dados incorretos')