produtos = {"banana": 10, "maçã": 30, "laranja": 18}

while True:
    print ("Produtos disponíveis:")
    for produto, qtd in produtos.items():
        print (f"- {produto}: {qtd}")

    escolha = input ("Digite o nome do produto que deseja comprar (ou 'sair' para encerrar): ").lower()
    if escolha == "sair":
        print ("Obrigado por comprar conosco!")
        break

    if escolha in produtos:
        quantidade = int(input ("Digite a quantidade desejada: "))
        if quantidade <= produtos[escolha]:
            total = produtos[escolha] * quantidade
            print (f"O total a pagar por {quantidade} {escolha}(s) é: R$ {total:.2f}")
            produtos[escolha] -= quantidade
            
        else:
            print ("Quantidade indisponível. Por favor, escolha uma quantidade menor.")

    else:
        print ("Produto não encontrado. Por favor, escolha um produto válido.")


    