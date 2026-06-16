litsa = []
continuar = "s" or "S" or "sim" or "SIM"

while continuar == "s" or continuar == "S" or continuar == "sim" or continuar == "SIM":
    nome = input("Digite o nome: ")
    litsa.append(nome)
    continuar = input("Deseja continuar? (s/n): ")

print(f"Os nomes digitados foram: {litsa}")