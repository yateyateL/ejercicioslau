valor_compra = int(input("valor de la compra: "))

if valor_compra >= 50000:
    balota = input("escoja una balota (roja, verde, azul, amarilla, negra): ")
    if balota == "roja":
        descuento = valor_compra*0.10
    elif balota == "verde":
        descuento = valor_compra*0.15
    elif balota == "azul":
        descuento = valor_compra*0.20
    elif balota == "amarilla":
        descuento = valor_compra*0.50
    elif balota == "negra":
        descuento = valor_compra*1.00
    valor_pagar = valor_compra - descuento
    print(f"Valor de la compra: {valor_compra}")
    print(f"Color de la balota: {balota}")
    print(f"Valor del descuento: {descuento}")
    print(f"Valor a pagar: {valor_pagar}")
else:
    print("si la compra es inferior a 50.000 pesos no participa en el sorteo")
    print(f"Valor a pagar: {valor_compra}")
    