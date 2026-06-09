estoque = [

    [12, 5, 8],

    [3, 15, 2],

    [19, 0, 7]

]

while True:
    numero = int(input("Digite o número da prateleira (1-3): "))
    item = int(input("Digite o número do item (1-3): "))
    if 1 <= numero <= 3 and 1 <= item <= 3:
        print(f"Quantidade em estoque: {estoque[numero-1][item-1]}")
    else:
        print("Entrada inválida. Tente novamente.")
