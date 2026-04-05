# Faça uma função chamada nota do aluno
# peça varias notas, e a situação e opcional
# tem que mostrar:
  # maior nota
  # menor nota
  # media 
  # total de notas
  # situação

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


resp = notaAluno(6, 5.5, 7, 10, 8, situação=True)
print(resp)