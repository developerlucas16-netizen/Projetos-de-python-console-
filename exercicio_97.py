# Faça um prgrama que faça uma linha com tamanho adptado da frase

def escreva(frase):
  cont = len(frase)
  print('~' * cont)
  print(frase)
  print('~' * cont)

texto = str(input('Digite a frase desejada: '))

escreva(texto)