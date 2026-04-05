letras = list()
passada = ''
cont = 0
total = 0

while True:
    atual = str(input("Digite uma letra: ")).upper()

    if atual != 'X':
        if atual == passada:
            cont += 1
            letras.append(atual)
            passada = atual
            total += 1
        else:
            passada = atual
            total += 1

    elif atual == "X":
        break


print(f'Foi digitado {total} letras, foram {cont} repetidas, e as letras foram {letras}')