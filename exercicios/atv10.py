import random

while True:
    try:
        random_number = random.randint(1, 20)
        
        numero = int(input("Digite um número inteiro: "))
        if numero == random_number:
            print("Parabéns! Você acertou o número aleatório!")
            break
        else:
            print (f"Que pena tente novamenta")
            
    except ValueError:
        print("Valor inválido. Por favor, digite um número inteiro.")