# peça um nunero de 0 a 9999
# mostre a unidade dezena centena milhar
# exemplo 1834
# unidade =  4; centena = 3; centena = 8; milhar = 1 

num = str(input('Digite um numero de 0 a 9999: '))

print(f"""
        seu numero foi {num}
        unidade = {num[3]}
        dezena = {num[2]}
        centena = {num[1]}
        milhar = {num[0]}
      """)