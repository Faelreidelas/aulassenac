campo = [

    ["~", "~", "~", "~", "~"],
    ["~", "~", "~", "~", "~"],
    ["~", "~", "~", "~", "~"],
    ["~", "~", "bomba", "~", "~"],


]
         
while True:
    linha = int(input("Digite a linha (1-4): "))
    coluna = int(input("Digite a coluna (1-5): "))

    print(f"Você escolheu a posição: {campo[linha-1][coluna-1]}")
    if campo[linha-1][coluna-1] == "bomba":
            print("Bomba encontrada! Fim de jogo.")
            break
    else:
            print("Posição segura. Continue jogando.")