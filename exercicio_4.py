#Pedir uma palavra
#Mostrar o tipo, os espaços, se numerico, se alfanumerico, se maisúsculo, se minúsculo, se capitalizado

palavra = input("Digite uma palavra: ")

print(f"O tipo primitivo desse valor é ", type(palavra))
print(f"Só tem espaços? ", palavra.isspace())
print(f"É um número? ", palavra.isnumeric())
print(f"É alfabetico? ", palavra.isalpha())
print(f"É alfanúmerico? ", palavra.isalnum())
print(f"Está em maiúsculo? ", palavra.isupper())
print(f"Está em minúsculo? ", palavra.islower())
print(f"Está capitalizada? ", palavra.istitle())