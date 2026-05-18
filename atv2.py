idade = float(input("digite a idade do atleta: "))

match idade:
    case x if idade < 5:
        print("atleta muito jovem")
    case x if idade < 10:
        print("atleta juvenil")
    case x if idade < 18:
        print("atleta adolescente")
    case x if idade < 30:
        print("atleta adulto")
    case x if idade < 50:
        print("atleta meio-idade")
    case  _:
        print("atleta idoso")  