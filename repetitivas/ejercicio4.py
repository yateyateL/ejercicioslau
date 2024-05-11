#Calcular e imprimir la tabla de multiplicar de un número cualquiera, el cual se digitará por teclado. Imprimir el multiplicando, el multiplicador y el producto.

    
numero= int(input("ingrese el numero de la tabla de multiplicar:"))
for i in range(1,20):
    print(f"{numero} x {i}={numero * i}")
    