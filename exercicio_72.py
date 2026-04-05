# Crie um progama que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
# Exemplo:
# Digite um número entre 0 e 20: 5 
numeros_extenso = ("zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove", "dez", "onze", "doze", "treze", "quatorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove", "vinte")
numero = int(input("Digite um número entre 0 e 20: "))
if 0 <= numero <= 20:
    print(f"O número {numero} por extenso é: {numeros_extenso[numero]}")
else:
    print("Número fora do intervalo permitido.")