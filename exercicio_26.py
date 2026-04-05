# peça uma frase
# MOstre quantos A temn nela
# mostre aonde esta o prinmeiro A
# Mostre aonde esta o ultimo A

frase = str(input('Digite uma frase: '))

if 'a' in frase:
    frase = frase.upper()
    frase = frase.strip()   
    print(f'''
Sua frase foi {frase.strip()}
Quantidade de A: {frase.count("A")}
Primeiro A: {frase.find('A') + 1}
Ultimo A: {frase.rfind('A') + 1}
      ''')
    
else:
    print('Não tem A na frase')