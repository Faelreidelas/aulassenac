tentativas = []
continuar = "s" or "S" or "sim" or "SIM" or "s" or "sIM" or "sIm" or "Sim"
senha = "123456"

while continuar == "s" or continuar == "S" or continuar == "sim" or continuar == "SIM" or continuar == "s" or continuar == "sIM" or continuar == "sIm" or continuar == "Sim":
    tentativa = input("Digite a senha: ")
    tentativas.append(tentativa)

    if tentativa == senha:
        print("Senha correta! Acesso concedido.")
        break
    else:
        print("Senha incorreta! Tente novamente.")
        continuar = input("Deseja continuar? (s/n): ")