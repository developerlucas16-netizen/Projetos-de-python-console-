import os
import math
import random
import time

# ============================
# Função pra limpar o console
# ============================
def limpar():
    os.system('cls' if os.name == 'nt' else 'clear')

# ============================
# Variavel do while principal
# ============================
cont = True
# ==================================
# Variavel do while do par ou impar
# ===================================
cont_2 = True
# ==================
# Varial do jokenpô
# ==================
cont_3 = True
# ==============================
# Variavel do adivinhe o número
# ==============================
cont_4 = True
# ==========================
# Variavel do jogo da velha
# ==========================
cont_5 = True
# ==================================
# Variavel do palavras embaralhadas
#===================================
cont_6 = True


while(cont):
    limpar()
    print(f'-----------------------------------------------------------')
    print(f'--------------------------JOGOS----------------------------')
    print(f'-----------------------------------------------------------')
    print(f'                                                           ')
    print(f' --> 1 Par ou Ímpar')
    print(f' --> 2 Jokenpô')
    print(f' --> 3 Adivinhe o número')
    print(f' --> 4 Jogo da velha')
    print(f' --> 5 Palavras emabaralhadas')
    print(f' --> 0 Sair')
    print(f'                                                           ')

    opcao = int(input('Digite sua opção: '))

    if(opcao < 0 or opcao > 5):
        print(f'Opção inválida, tente novamente')
        time.sleep(2)

    limpar()

# ==========================
# Estrutura do par ou impar
# ==========================
    match opcao:
        case 1:
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
                        break
# =====================
# Estrutura do jokenpô
# =====================
        case 2:
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
# ===============================
# Estrutura do adivinhe o número
# ===============================
        case 3:
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

# ===========================
# Estrutura do jogo da velha
# ===========================
        case 4:
            while(cont_5):
                limpar()
                print(f'-------------------------------------------------')
                print(f'------------------JOGO DA VELHA------------------')
                print(f'-------------------------------------------------')
                print(f'                                                 ')
                print(f' --> 1 Jogar')
                print(f' --> 0 Voltar')

                opcao_5 = int(input('Digite sua opção: '))

                match opcao_5:
                    case 1:
                        def print_board(board):
                            for row in board:
                                print(' | '.join(row))
                                print('-' * 9)
                    
                        def check_winner(board, player):
                            for row in board:
                                if all(s == player for s in row):
                                    return True
                            for col in range(3):
                                if all(board[row][col] == player for row in range(3)):
                                    return True
                            if all(board[i][i] == player for i in range(3)):
                                return True
                            if all(board[i][2 - i] == player for i in range(3)):
                                return True
                            return False
                        
                        tabuleiro = [[' ' for _ in range(3)] for _ in range(3)]
                        jogador_atual = 'X'

                        for _ in range(9):
                            print_board(tabuleiro)
                            print(f'Jogador {jogador_atual}, é sua vez!')
                            linha = int(input('Digite a linha (0, 1, 2): '))
                            coluna = int(input('Digite a coluna (0, 1, 2): '))
                            time.sleep(2)
                            limpar()

                            if tabuleiro[linha][coluna] == ' ':
                                tabuleiro[linha][coluna] = jogador_atual
                                if check_winner(tabuleiro, jogador_atual):
                                    print_board(tabuleiro)
                                    print(f'Parabéns, jogador {jogador_atual} ganhou!!!')
                                    time.sleep(5)
                                    limpar()
                                    break
                                jogador_atual = 'O' if jogador_atual == 'X' else 'X'
                            else:
                                print('Posição já ocupada, tente novamente.')
                        else:
                            print_board(tabuleiro)
                            print('Empate!!!')
                            time.sleep(5)
                            limpar()
                    case 0:
                        limpar()
                        break

# ===================================
# Estrutura do palavras embaralhadas
# ===================================
        case 5:
            while(cont_6):
                limpar()
                print(f'-------------------------------------------------')
                print(f'-------------PALAVRAS EMBARALHADAS--------------')
                print(f'-------------------------------------------------')
                print(f'                                                 ')
                print(f' --> 1 Jogar')
                print(f' --> 0 Voltar')

                opcao_6 = int(input('Digite sua opção: '))

                match opcao_6:
                    case 1:
                        palavras = [
                                    "casa", "vento", "mar", "sol", "lua", "estrela", "rio", "montanha", "floresta", "nuvem",
                                    "chuva", "fogo", "terra", "areia", "pedra", "campo", "cidade", "estrada", "ponte", "janela",
                                    "porta", "livro", "caneta", "papel", "mesa", "cadeira", "computador", "teclado", "mouse", "tela",
                                    "copo", "garrafa", "prato", "colher", "garfo", "faca", "mochila", "sapato", "camisa", "calça",
                                    "relógio", "telefone", "rádio", "televisão", "filme", "música", "arte", "foto", "quadro", "mapa",
                                    "jardim", "praça", "parque", "praia", "ilha", "barco", "avião", "carro", "ônibus", "bicicleta",
                                    "amigo", "família", "criança", "adulto", "idoso", "professor", "aluno", "médico", "engenheiro", "artista",
                                    "cachorro", "gato", "pássaro", "peixe", "cavalo", "leão", "tigre", "urso", "elefante", "macaco",
                                    "banana", "maçã", "uva", "laranja", "morango", "abacaxi", "melancia", "limão", "pêssego", "pera",
                                    "feliz", "triste", "rápido", "lento", "quente", "frio", "claro", "escuro", "forte", "fraco"
                                    ]      
                        palavra = random.choice(palavras)
                        escolhida = palavra
                        palavra_embaralhada = ''.join(random.sample(palavra, len(palavra)))

                        limpar()
                        
                        tentativas = 3
                        while tentativas > 0: 
                            print(f'Vamos começar!!!')
                            print(f'                                                 ')
                            print(f'Qual é a palavra embaralhada?')
                            print(f'                                                 ')
                            print(f'Palavra embaralhada: {palavra_embaralhada}')
                            print(f'                                                 ')
                            print(f'Chance: {tentativas} tentativas')
                            chute = str(input('Digite sua resposta: ')).lower()

                            if  chute == escolhida:
                                print(f'Parabéns, você acertou a palavra!!!')
                                time.sleep(5)
                                limpar()
                                break
                            
                            elif chute != escolhida and tentativas > 0:
                                print(f'Quase, vamos la não desanime!! Mais {tentativas} tentativas')
                                tentativas -= 1
                                print(f'                                                ')
                                time.sleep(5)
                            
                            elif chute != escolhida and tentativas == 0:
                                limpar()
                                print(f'Vishhh, mais sorte na proxima vez!!! A palavra era {escolhida}')
                                time.sleep(3)
                                limpar()
                                break
                    case 0:
                        limpar()
                        break

        case 0:
            print(f'Voce quer sair ?')
            limpar()
            break


