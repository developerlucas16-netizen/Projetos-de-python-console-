import os
import time
import random

def limpar():
    os.system('cls' if os.name == 'nt' else 'clear')

cont_3 = True

limpar()
while(cont_3):
    print(f'--------------------------------------------------')    
    print(f'---------------------JOKENPÔ----------------------')
    print(f'--------------------------------------------------')
    print(f'                                                  ')
    print(f' --> 1 Jogar')
    print(f' --> 2 Voltar') 
    opcao_3 = int(input('Digite sua opção: '))

    match opcao_3:
        case 1:
            limpar()
            print(f'Vamos começar!!!')
            print(f'Escolha pedra, papel ou tesoura')
            escolha_1 = str(input('Digite sua escolha: ')).lower()
            escolha_maq = random.choice(['pedra', 'papel', 'tesoura'])
            time.sleep(2)
            limpar()
                        
            print(f'JOO')
            time.sleep(1)
            print(f'KEEEN')
            time.sleep(1)
            print(f'PÔÔÔ')
            time.sleep(1)

            limpar()

            print(f'Você escolheu {escolha_1} e a maquina escolheu {escolha_maq}')

            # ----------------------------------------
            # Escolhas quando o jogador escolhe pedra
            # ----------------------------------------
            if escolha_1 == 'pedra' and escolha_maq == 'tesoura':
                print(f'Parabéns, você ganhou!!!')
                time.sleep(6)
                limpar()

            elif escolha_1 == 'pedra' and escolha_maq == 'papel':
                print(f'Vishhh, mais sorte na proxima vez!!!')
                time.sleep(6)
                limpar()
                        
            elif escolha_1 == 'pedra' and escolha_maq == 'pedra':
                print(f'Eita kkkkkkkk, deu empate!!!')
                time.sleep(6)
                limpar()

            # ----------------------------------------
            # Escolhas quando o jogador escolhe papel
            # ----------------------------------------
            elif escolha_1 == 'papel' and escolha_maq == 'pedra':
                print(f'Parabens você ganhou!!!')
                time.sleep(6)
                limpar()
                        
            elif escolha_1 == 'papel' and escolha_maq == 'tesoura':
                print(f'Vishhh, mais sorte na proxima vez!!!')
                time.sleep(6)
                limpar()
                        
            elif escolha_1 == 'papel' and escolha_maq == 'papel':
                print(f'Eita kkkkkkkk, deu empate!!!')
                time.sleep(6)
                limpar()
                        
            # ------------------------------------------
            # Escolhas quando o jogador escolhe tesoura
            # ------------------------------------------
            elif escolha_1 == 'tesoura' and escolha_maq == 'papel':
                print(f'Parabens você ganhou!!!')
                time.sleep(6)
                limpar()    
                        
            elif escolha_1 == 'tesoura' and escolha_maq == 'pedra':
                print(f'Vishhh, mais sorte na proxima vez!!!')
                time.sleep(6)
                limpar()
                        
            elif escolha_1 == 'tesoura' and escolha_maq == 'tesoura':
                print(f'Eita kkkkkkkk, deu empate!!!')
                time.sleep(6)
                limpar()
                        
        case 0:
            limpar()
            break