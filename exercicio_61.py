# faça uma progressão aritmética, onde o usuário digite o primeiro termo e a razão, mostrando os 10 primeiros termos da progressão  
print('Gerador de PA')
primeiro_termo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
decimo_termo = primeiro_termo + (10 - 1) * razao
for c in range(primeiro_termo, decimo_termo + razao, razao):
    print(c, end=' -> ')  
print('FIM')  