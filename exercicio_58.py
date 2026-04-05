# Tente acertar o numero

import random

cont = True
tenta = 1
num_1 = [0,1,2,3,4,5,6,7,8,9,10]
num = random.choice(num_1)

print(f'''
Sou seu computador
acabei de pensar em um numero de 0 a 10
Voce consegue adivinhar qual foi ?
''')

while(cont):
  kick = int(input('Qual seu palpite: '))

  if kick == num:
    print(f'Parabens, você conseguiu em {tenta} tentativas')

    if num < kick:
      print(f'Um pouco menos... Vamos la')
    
    elif num > kick:
      print(f'Um pouco mais... Vamos la')