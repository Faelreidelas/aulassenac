while True: 
    acess = (input("Digite um acesso: "))
    acess = acess.lower()

    match acess:
        case "admin":
            print("Acesso total: Criar, Ler, Atualizar e Deletar")
        case "gerente":
            print("Acesso gerencial: Criar, Ler e Atualizar")
        case "visitante":
            print("Acesso restrito: Apenas Leitura")
        case _:
            print("acesso bloqueado. Tente novamente.")