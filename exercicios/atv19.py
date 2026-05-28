listasnumeros = []

while True:
    numero = input("Digite um número (ou 'sair' para encerrar): ")
    if numero.lower() == "sair" or numero == "0":
        print("Encerrando o programa.")
        break
    listasnumeros.append(int(numero))

print("soma Números digitados:", sum(listasnumeros))