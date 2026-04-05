# Fazer um menu que tenha soma multiplicar maior novos numeros e sair do programa

def menu():
    print('1 - Somar')
    print('2 - Multiplicar')
    print('3 - Maior')
    print('4 - Novos números')
    print('5 - Sair do programa') 

def main():
    while True:
        menu()
        opcao = int(input('Escolha uma opção: '))
        
        if opcao == 1:
            num1 = float(input('Digite o primeiro número: '))
            num2 = float(input('Digite o segundo número: '))
            resultado = num1 + num2
            print(f'A soma é: {resultado}')
        
        elif opcao == 2:
            num1 = float(input('Digite o primeiro número: '))
            num2 = float(input('Digite o segundo número: '))
            resultado = num1 * num2
            print(f'A multiplicação é: {resultado}')
        
        elif opcao == 3:
            num1 = float(input('Digite o primeiro número: '))
            num2 = float(input('Digite o segundo número: '))
            maior = max(num1, num2)
            print(f'O maior número é: {maior}')
        
        elif opcao == 4:
            continue
        
        elif opcao == 5:
            print('Saindo do programa...')
            break
        
        else:
            print('Opção inválida. Tente novamente.')