listaProdutos = []


while True:
    produto = input("Digite um produto: ")
    listaProdutos.append(produto)
    continuar = input("Deseja continuar? (S/N): ")
    if continuar.upper() == "N":
        break

listaProdutos.sort(key=str.lower)       
print("Produtos em ordem alfabética:", listaProdutos)
