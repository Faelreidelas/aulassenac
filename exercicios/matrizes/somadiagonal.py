matriz_quadrada = [

    [5, 2, 9],

    [1, 8, 3],

    [4, 7, 6]

]

while True:
    diagonal = int(input("Digite a posição da diagonal (1-3): "))
    vari = diagonal - 1
    
    if 1 == diagonal :
        print(f"A soma da diagonal é: {matriz_quadrada[0][vari] + matriz_quadrada[1][vari + 1] + matriz_quadrada[2][vari + 2]}")
    
    elif 2 == diagonal :
        print("so na diagonal animal)")

    elif diagonal == 3:
        print(f"A soma da diagonal é: {matriz_quadrada[0][vari] + matriz_quadrada[1][vari - 1] + matriz_quadrada[2][vari - 2]}")    

    else:diagonal != 1 or diagonal != 2 or diagonal != 3
    print("Entrada inválida. Tente novamente.")