#crie um jogo de par ou impar
import random
import time
import os   

def limpar():
    os.system('cls' if os.name == 'nt' else 'clear')

cont_2 = True

limpar()
while(cont_2):
                print(f'--------------------------------------------------')
                print(f'------------------PAR OU ÍMPAR--------------------')
                print(f'--------------------------------------------------')
                print(f'                                                  ')
                print(f' --> 1 Jogar')
                print(f' --> 0 Voltar')
                opcao_2 = int(input('Digite sua opção: '))

                match opcao_2:
                    case 1:
                        limpar()
                        print(f'Vamos comerçar!!!!')
                        print(f'A mquina te deixou começar, escolha par ou impar')
                        escolha_1 = str(input('Digite par ou impar: ')).lower()

                        if escolha_1 == 'par':
                            escolha_maq = 'impar'
                        
                        elif escolha_1 == 'impar':
                            escolha_maq = 'par'

                        print(f'Ok OK, Agora um número de 0 a 10')
                        escolha_num = int(input('Digite um número: '))
                        num_maq = random.randint(0, 10)
                        time.sleep(2)
                        print(f'Vamos ver o resultado...')
                        soma = escolha_num + num_maq
                        time.sleep(2)

                        limpar()

                        print(f'Bom, você escolheu {escolha_1} e a maquina escolheu {escolha_maq}')
                        print(f'Você escolheu o número {escolha_num} e a maquina escolheu o número {num_maq}')
                        time.sleep(2)
                        print(f'Vamos ao resultado...')
                        time.sleep(2)

                        if (soma % 2 == 0 and escolha_1 == 'par'):
                            print(f'Parabéns, você ganhou!!!')
                            time.sleep(10)
                            limpar()
                
                        elif(soma % 2 != 0 and escolha_1 == 'par'):
                            print(f'Vishhh, mais sorte na proxima vez!!!')
                            time.sleep(10)
                            limpar()
                
                        elif(soma % 2 == 0 and escolha_1 == 'impar'):
                            print(f'Vishhh, mais sorte na proxima vez!!!')
                            time.sleep(10)
                            limpar()
                
                        elif(soma % 2 != 0 and escolha_1 =='impar'):
                            print(f'Parabéns, você ganhou!!!')
                            time.sleep(10)
                            limpar()
                    
                    case 0:
                        limpar()
                        cont_2 = False
                        break