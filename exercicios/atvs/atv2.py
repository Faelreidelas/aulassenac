listant = []
continuar = "s"
contador = 1

while continuar == "s" or continuar == "S" or continuar == "sim" or continuar == "SIM" or continuar == "Sim" or continuar == "sIM":
    nome = int(input(f"Digite a nota {contador}: "))
    listant.append(nome)
    contador += 1
    continuar = input("Deseja continuar? (s/n): ")

print(f"A média das notas digitadas foi: {sum(listant) / len(listant) if listant else 0}")
