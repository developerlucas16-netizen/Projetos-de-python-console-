#Pedir 3 notas
#Caulcular a média
#Mostrar como o aluno ficou no final

nota_1 = float(input("Digite a primeira nota: "))
nota_2 = float(input("Digite a segunda nota: "))
nota_3 = float(input("Digite a terceira nota: "))

soma = nota_1 + nota_2 + nota_3

media = soma / 3

print(f"Suas notas forma as seguinte")
print(f"1ª: {nota_1}")
print(f"2ª: {nota_2}")
print(f"3ª: {nota_3}")
print(f"Com tudo sua média foi de {media}")

if(media < 6) :
    print(f"Desculpe mas você não atingiu a média...")

if(media == 6 or media == 7) :
    print(f"Ufa !!! Por pouco.")

else :
    print(f"Parabens você passou com sobra")
