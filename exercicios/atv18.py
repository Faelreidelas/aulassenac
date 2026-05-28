while True:
    digite = input("sair ou continuar: ")
    if digite.lower() == "sair":
        print("Encerrando o programa.")
        break
    digito = int(input("Digite um número inicial: "))
    digito2 = int(input("Digite um número final: "))
    pulo = int(input("Digite o valor do salto: "))
    impressao = digito + pulo
    if digito2 < digito:
        print("O número final deve ser maior que o número inicial.")
    elif pulo <= 0:
        print("O valor do salto deve ser maior que zero.")


    elif digito2 == digito:
        print("O número final deve ser diferente do número inicial.")

    elif digito2 > digito and pulo > 0:
        while impressao <= digito2:
            print(impressao)
            impressao += pulo
    else:
        print("digite um número válido.")

    

    
    