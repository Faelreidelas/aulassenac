while True: 
    nota = (input("Digite uma nota: "))
    nota = nota.lower()

    match nota:
        case "a":
            print("Nota A excelente")
        case "b":
            print("Nota B boa")
        case "c":
            print("Nota C regular")
        case "d":
            print("Nota D ruim")
        case "f":
            print("Nota F reprovado")
        case _:
            print("Nota inválida. Tente novamente.")