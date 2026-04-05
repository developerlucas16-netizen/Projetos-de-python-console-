# Peça o nome completo
# Nome com todas as leqtras maiúsculas
# Nome com todas as letras minúsculas
# Quantas letras tem o nome (sem considerar os espaços)
# Quantas letras tem o primeiro nome

nome_completo = str(input('Digite seu nome completo:'))

print(f"""
        Nome completo: {nome_completo}
        Nome com todas a letras maiusculas: {nome_completo.upper()}
        Nome com todas a letras minusculas: {nome_completo.lower()}
        Nome sem considerar os espaços: {len(nome_completo.replace(' ', ''))}
        Quantidade de letras do primeiro nome: {len(nome_completo.split()[0])}
      """)