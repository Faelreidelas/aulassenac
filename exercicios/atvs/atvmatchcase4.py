while True: 
    codigo = (input("Digite um codigo: "))

    match codigo:
        case "101":
            print("sanduiche 12R$ ")
        case "102":
            print("batata frita 8R$")
        case "103":
            print("refrigerante 5R$")
        case _:
            print("Código inválido. Tente novamente.")