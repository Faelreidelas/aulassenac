vendas = [

    [1200, 850, 900, 1500],

    [900, 1100, 1000, 1300],

    [1500, 1600, 1400, 1800],

    [700, 600, 800, 900]

]

while True:
    
    print("dias disponíveis: domingo, segunda, terça, quinta")
    print("vendedores disponíveis: rob, ana, carlos, maria")

    dia = int(input("Digite o dia (1-4): "))
    vendedor = int(input("Digite o numero do vendedor de  (1-4): "))

    print(f"o valor vendido por : ", vendas[dia-1][vendedor-1])

    if input("Deseja consultar outra venda? (s/n): ").lower() != 's':
        break
    
    elif dia < 1 or dia > 4 or vendedor < 1 or vendedor > 4:
        print("Entrada inválida. Tente novamente.")
        