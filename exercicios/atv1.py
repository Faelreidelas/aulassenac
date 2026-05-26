listnmr = []

for i in range(1,7):
    numero = int(input(f"Digite o {i}º número: "))
    listnmr.append(numero)

print (f"os números digitados são: {listnmr}")
print (f"a soma dos números digitados é: {sum(listnmr)}")
print (f"o maior e o menor dos números digitados é: {max(listnmr)} e {min(listnmr)} ")