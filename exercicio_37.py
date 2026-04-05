# Peça um numero
# Pergunte em qual opção ele quer converter
# 1 -> binario
# 2 ->octal
# 3 -> hexadecimal

import math

num = int(input('Digite um numero: '))


print('''
------------------------------------
             Convertor
------------------------------------
1 -> Binário
2 -> Octal
3 -> Hexadecimal
''')
escolha = int(input('Digite sua opção: '))

match escolha:
        case 1: 
            binario = bin(num)
            print(binario)
        
        case 2:
            octal = oct(num)
            print(octal)
        
        case 3:
            hexadecimal = hex(num)
            print(hexadecimal)
