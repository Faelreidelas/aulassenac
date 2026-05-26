while True:
    try:
        print("1-SOMAR")
        print("2-SUBTRAIR")
        print("3-MULTIPLICAR")
        print("4-DIVIDIR")
        print("5-ENCERRAR")
        opcao = int(input("Escolha uma opção: "))
        
        if opcao == 5:
            print("Encerrando o programa...")
            break
        
    except ValueError:
        print("Valor inválido. Por favor, digite um número inteiro.")