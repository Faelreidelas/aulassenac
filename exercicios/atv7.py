nota = int(input("Digite a nota do aluno: "))

while nota:
    if nota > 10 or nota < 0:
        print("digite novamente a nota do aluno")
        nota = int(input("Digite a nota do aluno: "))
    
    else:
        print(f"A nota do aluno é: {nota}")
        break