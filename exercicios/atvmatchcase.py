vogais = ['a', 'e', 'i', 'o', 'u']
consoantes = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']


while True:
    digito = input("digite uma letra : ")
    
    digito = digito.lower()

    match digito:
        case z if digito.lower() == '0':
            print("Encerrando o programa.")
            break
        case x if digito.lower() in vogais:
            print("Vogal digitada: ", digito)
        case y if digito.lower() in consoantes:
            print("Consoante digitada: ", digito)
        case _:
            print("Caractere inválido.")
