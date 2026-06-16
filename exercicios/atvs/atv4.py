listaid = []
continuar = "s" or "S" or "sim" or "SIM"

while continuar == "s" or continuar == "S" or continuar == "sim" or continuar == "SIM":
    idade = int(input("Digite o ano de nascimento: "))
    listaid.append(idade)
    continuar = input("Deseja continuar? (s/n): ")
    if idade > 2008:
        print("Maior de idade")
    else:
        print("Menor de idade")

    