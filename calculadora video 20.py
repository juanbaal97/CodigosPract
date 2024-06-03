print("programa calculadora con una variable")
print("********************")
print("* Menu de opciones *")
print("********************")

print('¿realizamos una operacion matemática?')

si = True
no = False
respuesta = str(input('Si o No: '))
respuesta = respuesta.lower()
while(respuesta == "si"):
    print("""
1. Suma
2. Resta
3. Multiplicación
4. División
5. División entera
6. Exponente
7. Modulo o resto """)
    numero = (int(input("cual es tu opcion deseada: ")))
    if numero == 1:
        print("Elegiste Suma.")
        numero = (int(input("introduce el primer numero: ")))
        numero += (int(input("introduce el segundo numero: ")))
        print("el resultado es: ",numero)
        print('¿Deseas realizar otra operacion?')
        respuesta = str(input('Si o No: '))
        respuesta = respuesta.lower()

    elif numero ==2:
        print("Elegiste Resta.")
        numero = (int(input("introduce el primer numero: ")))
        numero -= (int(input("introduce el segundo numero: ")))
        print("el resultado es: ",numero)
        print('¿Deseas realizar otra operacion?')
        respuesta = str(input('Si o No: '))
        respuesta = respuesta.lower()

    elif numero ==3:
        print("Elegiste Multiplicación.")
        numero = (int(input("introduce el primer numero: ")))
        numero *= (int(input("introduce el segundo numero: ")))
        print("el resultado es: ",numero)
        print('¿Deseas realizar otra operacion?')
        respuesta = str(input('Si o No: '))
        respuesta = respuesta.lower()

    elif numero ==4:
        print("Elegiste División.")
        numero = (int(input("introduce el primer numero: ")))
        numero /= (int(input("introduce el segundo numero: ")))
        print("el resultado es: ",numero)
        print('¿Deseas realizar otra operacion?')
        respuesta = str(input('Si o No: '))
        respuesta = respuesta.lower()

    elif numero ==5:
        print("Elegiste división entera.")
        numero = (int(input("introduce el primer numero: ")))
        numero //= (int(input("introduce el segundo numero: ")))
        print("el resultado es: ",numero)
        print('¿Deseas realizar otra operacion?')
        respuesta = str(input('Si o No: '))
        respuesta = respuesta.lower()

    elif numero == 6:
        print("Elegiste exponente.")
        numero = (int(input("introduce el primer numero: ")))
        numero **= (int(input("introduce el segundo numero: ")))
        print("el resultado es: ",numero)
        print('¿Deseas realizar otra operacion?')
        respuesta = str(input('Si o No: '))
        respuesta = respuesta.lower()

    elif numero == 7:
        print("Elegiste moudulo o resto.")
        numero = (int(input("introduce el primer numero: ")))
        numero %= (int(input("introduce el segundo numero: ")))
        print("el resultado es: ",numero)
        print('¿Deseas realizar otra operacion?')
        respuesta = str(input('Si o No: '))
        respuesta = respuesta.lower()
    else:
        print("no existe esa opción.")

else:
    print('Adios!!')

