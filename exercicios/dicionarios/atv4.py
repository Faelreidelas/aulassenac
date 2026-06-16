produtos = {"banana": 2.5, "maçã": 3.0, "laranja": 1.8}

while True:
    print ("Produtos disponíveis:")
    for produto, preco in produtos.items():
        print (f"- {produto}: R$ {preco:.2f}")

    escolha = input ("Digite o nome do produto que deseja comprar (ou 'sair' para encerrar): ").lower()
    if escolha == "sair":
        print ("Obrigado por comprar conosco!")
        break

    if escolha in produtos:
        quantidade = int(input ("Digite a quantidade desejada: "))
        total = produtos[escolha] * quantidade
        print (f"O total a pagar por {quantidade} {escolha}(s) é: R$ {total:.2f}")

    else:
        print ("Produto não encontrado. Por favor, escolha um produto válido.")


