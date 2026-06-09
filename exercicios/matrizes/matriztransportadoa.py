matriz_A = [
    [1, 2, 3],
    [4, 5, 6]
]

while True:
    print ("Matriz A:")
    for coluna in matriz_A:
        print(coluna)

    vari = int(input("Digite a coluna (1-3): "))
    matriztransposta = vari - 1
    print(f"a matriz é: {matriz_A[0][matriztransposta]}, {matriz_A[1][matriztransposta]}")
