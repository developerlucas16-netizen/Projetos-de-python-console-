# Faça um progrma que so aceite quando eu digito uma cidade com o nome que comece com santo
# Faça todas as correções possiveis

cidade = str(input('Em qual cidade você nasceu: '))

cidade.title()
cidade.strip()
primeira = cidade[0:5]

if primeira == 'Santo':
    print(f'True')

else:
    print(f'False')