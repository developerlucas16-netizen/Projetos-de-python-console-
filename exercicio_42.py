# Crie um programa que leia 3 retas e diga se ela pode formar um triangulo

# Entrada
a = float(input("Digite o primeiro lado (cm): "))
b = float(input("Digite o segundo lado (cm): "))
c = float(input("Digite o terceiro lado (cm): "))

# Validação de valores positivos
if a <= 0 or b <= 0 or c <= 0:
    print("Os lados devem ser maiores que zero ❌")
else:
    # Verifica se forma triângulo
    if a + b > c and a + c > b and b + c > a:
        print("FORMA um triângulo ✅")

        # ======================
        # Classificação pelos lados
        # ======================
        if a == b == c:
            print("Triângulo EQUILÁTERO")
        elif a == b or a == c or b == c:
            print("Triângulo ISÓSCELES")
        else:
            print("Triângulo ESCALENO")

        # ======================
        # Classificação pelos ângulos
        # ======================
        # Organiza para facilitar (maior lado por último)
        lados = sorted([a, b, c])
        x, y, z = lados  # z é o maior lado

        if x**2 + y**2 == z**2:
            print("Triângulo RETÂNGULO")
        elif x**2 + y**2 > z**2:
            print("Triângulo ACUTÂNGULO")
        else:
            print("Triângulo OBTUSÂNGULO")

    else:
        print("NÃO forma um triângulo ❌")
