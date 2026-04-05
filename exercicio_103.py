# Faça  uma função chamada ficha
# peça como parametro o nome do jogador e quntos gols ele fez
# coloque paremtros opcionais para erros

def ficha(nome = '<desconhecido>',gols=0):
  """
  -> nome = É o nome do jogador que o usuário digitar
  -> gols = e a quantidade de gols que ele fez 
  """
  if nome == "":
    nome = "<desconhecido>"

  frase = print(f"O nome do jogador é {nome} e ele fez {gols} gols na partidade")

  return frase


name = str(input('Digite o nome do jogador: \n'))
quantos = str(input('Quantos gols ele fez na partida: \n'))

if quantos.isnumeric():
  quantos = int(quantos)
else:
  quantos = 0

ficha(name, quantos)