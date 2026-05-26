while True:
    try:
        valor = int(input("Digite o valor para sacar (apenas valores pares): "))

        if valor <= 0 or valor % 2 != 0:
            print("Valor inválido. Por favor, digite um valor positivo e divisível por 2.")
            continue

        notas = [50, 20, 10, 2]
        contadoes = {}
        restante = valor

        for nota in notas:
            quantidade = restante // nota
            if quantidade:
                contadoes[nota] = quantidade
                restante -= quantidade * nota

        if restante != 0:
            print("Não foi possível sacar o valor com as notas disponíveis.")
        else:
            print(f"Saque de R$ {valor} realizado com sucesso!")
            for nota in notas:
                if nota in contadoes:
                    print(f"{contadoes[nota]} nota(s) de R$ {nota}")
            break

    except ValueError:
        print("Valor inválido. Por favor, digite um número inteiro.")