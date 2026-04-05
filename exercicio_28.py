# Faça o computador sortear um numero
# e peça para o usuario adivinhar qual foi o numero sorteado
import random
import time
import os   
def limpar():
    os.system('cls' if os.name == 'nt' else 'clear')

cont_4 = True

while(cont_4):
                limpar()
                print(f'-------------------------------------------------')
                print(f'----------------ADIVINHE O NÚMERO----------------')
                print(f'-------------------------------------------------')
                print(f'                                                 ')
                print(f' --> 1 Jogar')
                print(f' --> 0 Voltar')

                opcao_4 = int(input('Digite sua opção: '))

                match opcao_4:
                    case 1:
                        limpar()
                        num = random.randint(0, 10)
                        print(f'Vamos começar!!!')
                        print(f'Escolha um número de 0 a 10')
                        escolha_1 = int(input('Digite sua escolha: '))
                        time.sleep(2)

                        limpar()

                        print(f'Vamos ver o resultado...')
                        time.sleep(2)

                        if escolha_1 == num:
                            print(f'Parabéns, você acertou o número!!!')
                            time.sleep(5)
                            limpar()
                        else:
                            print(f'Vishhh, mais sorte na proxima vez!!! O número era {num}')
                            time.sleep(5)
                            limpar()
                        
                    case 0:
                        limpar()
                        break