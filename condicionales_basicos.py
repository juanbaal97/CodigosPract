 #programa del video N.10
print("bienvenido al programa de entrega de calificaciones")
nombre = input("¿cual es tu nombre?: ")

num_one = int(input("ingrese la cantidad de creditos de todo su curso: "))


operacion = round((num_one * 0.10)/6,1)

if operacion > 7:
    print("FELICIDADES!," + nombre + " ESTAS APROVADO, CON UN PROMEDIO DE: ", operacion)
else:
    print("REPROVADO. CON UN PROMEDIO DE: ", operacion)
    
