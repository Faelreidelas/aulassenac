funcionario = input ("digite o nome do funcionario : ")
salario = float(input ("digite o salario do funcionario : "))
emprestimo = float(input ("digite o valor do emprestimo : "))
score = salario * 0.3


if emprestimo > score:
    print ("emprestimo reprovado")

else:
    print ("emprestimo aprovado")