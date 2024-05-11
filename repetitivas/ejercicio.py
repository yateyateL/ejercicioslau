#leer 20 números e imprimir cuantos son positivos cuantos negativos y cuantos neutros 

positivos=0
negativos=0
neutros=0
for _ in range(20):
   número= int(input("ingrese un número:"))
   if número > 0:
       positivos += 1
   elif número < 0:
       negativos += 1
   else:
       neutros += 1
       
print("cantidad de numeros positivos:", positivos)
print("cantidad de numeros negativos:", negativos)
print("cantidad de numeros neutros:", neutros)

       
       
       
       
   
        
               