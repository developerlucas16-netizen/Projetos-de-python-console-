#Pedir um valor em metros
#Converter para dm, cm, mm, dam, hm, km

valor = int(input("Digite um valor em metros: "))

dm = valor * 10
cm = valor * 100
mm = valor * 1000
dam = valor / 10
hm = valor / 100
km = valor / 1000

print(f"O valor digitado foi {valor}, e sua conversão será de: ")
print(f"MM = {mm}")
print(f"CM = {cm}")
print(f"DM = {dm}")
print(f"DAM = {dam}")
print(f"HM = {hm}")
print(f"KM = {km}")

