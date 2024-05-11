
menor_50 = 0
entre_50_y_70 = 0
entre_70_y_80 = 0
mayor_80 = 0

for _ in range(10):

    calificacion = int(input("Ingrese la calificación del estudiante (entre 1 y 100): "))
    
    # Validamos que la calificación esté entre 1 y 100
    while calificacion < 1 or calificacion > 100:
        print("Calificación inválida. Debe estar entre 1 y 100.")
        calificacion = int(input("Ingrese la calificación del estudiante (entre 1 y 100): "))
    
    # Determinamos en qué rango se encuentra la calificación y actualizamos los contadores
    if calificacion < 50:
        menor_50 += 1
    elif calificacion < 70:
        entre_50_y_70 += 1
    elif calificacion < 80:
        entre_70_y_80 += 1
    else:
        mayor_80 += 1

# Imprimimos resultados
print(f"Cantidad de estudiantes con calificación menor a 50: {menor_50}")
print(f"Cantidad de estudiantes con calificación entre 50 y 70: {entre_50_y_70}")
print(f"Cantidad de estudiantes con calificación entre 70 y 80: {entre_70_y_80}")
print(f"Cantidad de estudiantes con calificación mayor o igual a 80: {mayor_80}")