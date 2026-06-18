loja = {
    "1": {"nome": "Teclado Mecânico", "preco": 250.00},
    "2": {"nome": "Mouse Sem Fio", "preco": 120.00},
    "3": {"nome": "Monitor 24 polegadas", "preco": 850.00}
}

Carrinho = {}

def calcular_preco_com_desconto(produto, desconto):
    if produto in loja:
        preco_original = loja[produto]["preco"]
        preco_com_desconto = preco_original * (1 - desconto / 100)
        return preco_com_desconto
    else:
        return "Produto não encontrado."
     

while True:
    print ("Menu:")
    print ("1. mostra produtos")
    print ("2. calcula preço com desconto")
    print ("3. adicionar produto ao carrinho ")
    print ("4. mostrar carrinho")
    print ("5. finaliar compra")
    print ("6. Sair")

    escolha = input("Escolha uma opção: ")
    if escolha == "1":
        print("Produtos disponíveis:")
        for produto, info in loja.items():
            print(f"{produto}: {info['nome']} - R${info['preco']:.2f}")
    elif escolha == "2":
        produto = input("Digite o código do produto: ")
        desconto = float(input("Digite o percentual de desconto: "))
        preco_final = calcular_preco_com_desconto(produto, desconto)
        print(f"O preço do {loja[produto]['nome']} com {desconto}% de desconto é: R${preco_final:.2f}")
    elif escolha == "3":
        codigo_produto = input("Digite o código do produto para adicionar ao carrinho: ")
        if codigo_produto in loja:
            quantidade = int(input("Digite a quantidade: "))
            if codigo_produto in Carrinho:
                Carrinho[codigo_produto] += quantidade
            else:
                Carrinho[codigo_produto] = quantidade
            print(f"{quantidade} unidades de {codigo_produto} adicionadas ao carrinho.")
        
    elif escolha == "4":
        print("Itens no carrinho:")
        for produto, quantidade in Carrinho.items():
            print(f"{loja[produto]['nome']}: {quantidade}")

    elif escolha == "5":
        print("Finalizando compra...")
        total = 0
        for produto, quantidade in Carrinho.items():
            preco = loja.get(produto, {}).get("preco", 0)
            total += preco * quantidade
        print(f"O total da compra é: R${total:.2f}")
        Carrinho.clear()
        print("Compra finalizada com sucesso!")
        
    elif escolha == "6":
        print("Saindo do programa.")
        break
    else:
        print("Opção inválida. Tente novamente.")