# Peça o ano de nascimento e veja a idade
# 9 anos = mirin
# 14 anos = infantil
# 19 anos = junior
# 25 anos = sênior
# acima = Master

ano = int(input('Qual seu ano de nascimento: '))

idade = 2026 - ano

if ano <= 9:
    print(f'Mirin')

elif ano <= 14:
    print(f'Infantil')

elif ano <= 19:
    print(f'Junior')

elif ano <= 25:
    print(f'Sênior')

else:
    print(f'Master')