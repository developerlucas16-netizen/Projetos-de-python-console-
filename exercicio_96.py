# Faça uma função que calcule a area

def area(l, c):
  area = l * c
  print(f'A largura é {l:.2f}mts e o comprimento {c:.2f}, portanto a area é {area}mts²')

larg = float(input("Digite a largura: \n"))
compri = float(input('Digite o comprimento: \n'))
area(larg, compri)