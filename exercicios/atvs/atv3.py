listan = []
continuar = "s" or "S" or "sim" or "SIM" or "Sim" or "sIM"
contador = 1

while continuar == "s" or continuar == "S" or continuar == "sim" or continuar == "SIM" or continuar == "Sim" or continuar == "sIM":
    numero = int(input(f"Digite o número {contador}: "))
    listan.append(numero)
    contador += 1
    continuar = input("Deseja continuar? (s/n): ")

pares = [num for num in listan if num % 2 == 0]
print(f"Os números pares digitados foram: {pares}")

impares = [num for num in listan if num % 2 != 0]
print(f"Os números ímpares digitados foram: {impares}")