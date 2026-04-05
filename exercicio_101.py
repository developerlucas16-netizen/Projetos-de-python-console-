# Crie uma função chamada vota que vai receber como parâmnetro o ano de nascimento, retornando umm valor literal 
# indicando se uma pessoa tem voto negado, opcional ou obrigatório nas eleições

# A) crie uma função chamada vota
# B) Peça a data de nascimento da pessoa 
# C) Caulcule a idade da pessoa
# D) Faça um return que:
  # se idade < 16 => negado
  # se idade == 16 ou idade == 17 => opcional 
  # se idade >= 18 => obrigatório

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

print("=-" * 30)
data_1 = int(input('Em qual ano você nasceu: '))
data_2 = int(input('Em qual ano você nasceu: '))
data_3 = int(input('Em qual ano você nasceu: '))
print("=-" * 30)

# data 1
if vota(data_1) == "Negado":
  print("Você tem ainda e jovem de mais")
elif vota(data_1) == "Opcional":
  print("Você ainda tem a opção de escolha")
elif vota(data_1) == "Obrigatório":
  print("Espero que ja tenha votado, se não aqui está a multa")

print("=-" * 30)

# data 2
if vota(data_2) == "Negado":
  print("Você ainda e jovem de mais")
elif vota(data_2) == "Opcional":
  print("Você ainda tem a opção de escolha")
elif vota(data_2) == "Obrigatório":
  print("Espero que ja tenha votado, se não aqui está a multa")

print("=-" * 30)

# data 3
if vota(data_3) == "Negado":
  print("Você ainda e jovem de mais")
elif vota(data_3) == "Opcional":
  print("Você ainda tem a opção de escolha")
elif vota(data_3) == "Obrigatório":
  print("Espero que ja tenha votado, se não aqui está a multa")

print("=-" * 30)