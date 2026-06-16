Produtos = {"COD1: notebook": 1250, "COD2: Asus rog phone 6": 3000, "COD3: laptop i5": 1800}

Carrinho = {}

def calcular_preco_com_desconto(produto, desconto):
    if produto in Produtos:
        preco_original = Produtos[produto]
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
        for produto, preco in Produtos.items():
            print(f"{produto}: R${preco:.2f}")
    elif escolha == "2":
        produto = input("Digite o nome do produto: ")
        desconto = float(input("Digite o percentual de desconto: "))
        preco_final = calcular_preco_com_desconto(produto, desconto)
        print(f"O preço do {produto} com {desconto}% de desconto é: R${preco_final:.2f}")
    elif escolha == "3":
        
        
    elif escolha == "4":
        print("Itens no carrinho:")
        for produto, quantidade in Carrinho.items():
            print(f"{produto}: {quantidade}")

    elif escolha == "5":
        
        pass
    elif escolha == "6":
        print("Saindo do programa.")
        break
    else:
        print("Opção inválida. Tente novamente.")