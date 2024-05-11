# Definir un valor inicial para la variable 'compra' que permita entrar en el ciclo
compra = 1

while compra > 0:
    # Leer el valor de la compra
    compra = float(input("Ingrese el valor de la compra: "))
    
    if compra >= 50000:
        # Leer el color de la balota
        balota = input("Ingrese el color de la balota (roja, verde, azul, amarilla, negra): ")
        
        # Evaluar el color de la balota y aplicar el descuento correspondiente
        if balota == "roja":
            descuento = 0.10
        elif balota == "verde":
            descuento = 0.15
        elif balota == "azul":
            descuento = 0.20
        elif balota == "amarilla":
            descuento = 0.50
        elif balota == "negra":
            descuento = 1.00
        else:
            print("Color de balota no válido")
            continue
        
        # Calcular el valor a pagar con descuento
        valor_a_pagar = compra - (compra * descuento)
    else:
        print("Compra inferior a 50,000 pesos. No participa en el sorteo.")
        valor_a_pagar = compra
    
    # Imprimir resultados
    print(f"Valor de la compra: {compra}")
    print(f"Color de la balota: {balota}")
    print(f"Descuento: {descuento * 100}%")
    print(f"Valor a pagar: {valor_a_pagar}")