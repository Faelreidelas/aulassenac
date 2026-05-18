compra = float(input ("digite o valor da compra : "))

match compra:
    case x if compra <= 100:
        print (f"compra de baixo valor: R$ {compra:.2f}")
    case x if compra >= 100 and compra <= 300:
        compras = compra * 0.95
        print (f"compra de valor médio: R$ {compras:.2f})")
    case x if compra >= 300 and compra <= 500:
        compras = compra * 0.90
        print (f"compra de valor médio: R$ {compras:.2f})")

    case  _:
        compras = compra * 0.85
        print (compras)

    