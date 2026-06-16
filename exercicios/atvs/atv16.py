turma = [ ["Ana", 8.0, 9.0], ["Pedro", 5.5, 6.0], ["Carlos", 7.5, 7.0] ] 

for aluno in turma:
    nome = aluno[0]
    nota1 = aluno[1]
    nota2 = aluno[2]
    
    media = (nota1 + nota2) / 2
    
    print(f"{nome} - Média: {media:.2f}")